import json
import re

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from Publications import citation, verify
from Publications.models import Publication, PublicationSubmission, PublicationUsage, normalize_doi


def _group_publications(papers, key):
    groups = {}
    for paper in papers:
        groups.setdefault(key(paper), []).append(paper)
    return [{'title': title, 'papers': members} for title, members in groups.items()]

@ensure_csrf_cookie
def publications_view(request):
    papers = list(Publication.objects.filter(published=True).prefetch_related('usages'))
    tabs = []
    for key, label in Publication.CATEGORY_CHOICES:
        items = [paper for paper in papers if paper.category == key]
        if key == Publication.MODELS:
            groups = _group_publications(items, lambda paper: paper.model_name)
        elif key == Publication.STUDIES:
            groups = _group_publications(items, lambda paper: str(paper.year))
        else:
            groups = _group_publications(items, lambda paper: '')
        tabs.append({'key': key, 'label': label, 'groups': groups, 'count': len(items)})
    active = next((tab['key'] for tab in tabs if tab['count']), tabs[0]['key'])
    return render(request, 'publications.html', {
        'citation_request': citation.CITE_REQUEST,
        'tabs': tabs,
        'active_tab': active,
        'kind_choices': Publication.KIND_CHOICES,
        'usage_options': PublicationUsage.objects.all(),
    })


def _check_payload(result):
    titles = {paper.doi: paper.title for paper in Publication.objects.filter(doi__in=list(result['cites']))}
    return {
        'ok': True,
        'found': result['found'],
        'unavailable': result['unavailable'],
        'accepted': result['accepted'],
        'kind': result['kind'],
        'title': result['title'],
        'journal': result['journal'],
        'year': result['year'],
        'access': result['access'],
        'cites': [{'doi': doi, 'title': titles.get(doi, doi), 'source': source} for doi, source in result['cites'].items()],
        'scopus': result['scopus'],
    }


def lookup_publication(request):
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'Please log in to submit a paper.'}, status=403)
    doi = normalize_doi(request.GET.get('doi', ''))
    if not re.match(r'^10\.\d{4,9}/\S+$', doi) or len(doi) > 200:
        return JsonResponse({'ok': True, 'found': False})
    return JsonResponse(_check_payload(verify.verify(doi)))


@require_POST
def submit_publication(request):
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'error': 'Please log in to submit a paper.'}, status=403)

    try:
        payload = json.loads(request.body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({'ok': False, 'error': 'The submission could not be read.'}, status=400)

    doi = normalize_doi(str(payload.get('doi', '')))
    note = str(payload.get('note', '')).strip()[:1000]
    usage_ids = [value for value in payload.get('usages', []) if isinstance(value, int)]

    if not re.match(r'^10\.\d{4,9}/\S+$', doi) or len(doi) > 200:
        return JsonResponse({'ok': False, 'error': 'Please enter a valid DOI, for example 10.1016/j.cscm.2026.e05829.'}, status=400)
    usages = list(PublicationUsage.objects.filter(pk__in=usage_ids))
    if not usages:
        return JsonResponse({'ok': False, 'error': 'Please select the AsphaltMine resources used in the publication.'}, status=400)
    if Publication.objects.filter(doi=doi).exists():
        return JsonResponse({'ok': False, 'error': 'This paper is already listed.'}, status=409)
    if PublicationSubmission.objects.filter(doi=doi, status=PublicationSubmission.PENDING).exists():
        return JsonResponse({'ok': False, 'error': 'This paper was already submitted and is waiting for review.'}, status=409)
    if PublicationSubmission.objects.filter(doi=doi, status=PublicationSubmission.REJECTED).exists():
        return JsonResponse({'ok': False, 'error': 'This paper was already reviewed and was not accepted.'}, status=409)
    if PublicationSubmission.objects.filter(user=request.user, status=PublicationSubmission.PENDING).count() >= 10:
        return JsonResponse({'ok': False, 'error': 'You have several submissions waiting for review. Please wait until they are reviewed.'}, status=429)

    result = verify.verify(doi)
    if not result['found']:
        if result['unavailable']:
            return JsonResponse({'ok': False, 'error': 'The check could not be done right now. Please try again later.'}, status=503)
        return JsonResponse({'ok': False, 'error': 'We could not find this DOI. Please check it.'}, status=404)
    if not result['accepted']:
        return JsonResponse({'ok': False, 'error': 'Only published journal articles, conference papers and book chapters are accepted.'}, status=400)
    if result['scopus'] is False:
        return JsonResponse({'ok': False, 'error': 'Only publications indexed in Scopus are accepted.'}, status=400)

    submission = PublicationSubmission.objects.create(
        user=request.user,
        doi=doi,
        note=note,
        title=(result['title'] or '')[:500],
        journal=(result['journal'] or '')[:300],
        year=result['year'] if isinstance(result['year'], int) else None,
        kind=result['kind'],
        access=result['access'],
        cites='\n'.join(result['cites']),
        scopus=result['scopus'],
        report='\n'.join(result['report'] + [note for note in [verify.prediction_models_note(any(usage.name == 'Used prediction models' for usage in usages), result)] if note]),
    )
    submission.usages.set(usages)

    recipients = list(
        User.objects.filter(is_staff=True, is_active=True)
        .exclude(email='')
        .values_list('email', flat=True)
    )
    if recipients:
        context = {
            'submitter': request.user,
            'doi': doi,
            'title': result['title'],
            'journal': result['journal'],
            'cites': ', '.join(Publication.objects.filter(doi__in=list(result['cites'])).values_list('title', flat=True)) or 'none found',
            'scopus': {True: 'yes', False: 'no', None: 'not checked'}[result['scopus']],
            'usages': ', '.join(usage.name for usage in usages),
            'note': note,
            'review_url': request.build_absolute_uri(reverse('admin:publications_publicationsubmission_changelist')),
        }
        send_mail(
            'Paper submission',
            render_to_string('Publications/submission_email.txt', context),
            None,
            recipients,
            fail_silently=True,
        )

    return JsonResponse({'ok': True, 'message': 'Thank you. The publication was checked and submitted for approval.'})
