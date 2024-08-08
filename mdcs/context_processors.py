""" Site-wide template context processors for AsphaltMine.
"""
from django.conf import settings


def app_version(request):
    """Exposes settings.APP_VERSION to every template as APP_VERSION.

    Bump the version in one place (settings.py) instead of editing the
    footer HTML for every release.
    """
    return {"APP_VERSION": getattr(settings, "APP_VERSION", "")}


def _once(function):
    cache = []

    def call():
        if not cache:
            cache.append(function())
        return cache[0]

    return call


def citation_notice(request):
    from Publications import citation
    from Publications.models import Publication
    from mdcs import citation_notices as notices

    return {
        "citation_before": notices.CITE_BEFORE,
        "citation_after": notices.CITE_AFTER,
        "citation_models_before": notices.MODELS_BEFORE,
        "citation_visual_before": notices.VISUAL_BEFORE,
        "citation_models_after": notices.MODELS_AFTER,
        "citation_link_text": notices.LINK_TEXT,
        "citation_models_link_text": notices.MODELS_LINK_TEXT,
        "citation_models_url": citation.PUBLICATIONS_PATH + "#models",
        "citation_foundation_url": citation.PUBLICATIONS_PATH + "#foundation",
        "citation_references": _once(lambda: citation.references(Publication.FOUNDATION)),
    }


def write_access_request(request):
    user = getattr(request, "user", None)
    if not user or not user.is_authenticated:
        return {}
    from mdcs.views import has_write_access_request

    return {"write_access_requested": lambda: has_write_access_request(user)}
