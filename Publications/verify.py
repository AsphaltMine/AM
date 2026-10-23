import csv
import os
import re
from functools import lru_cache
from urllib.parse import quote

import requests
from django.conf import settings
from django.core.cache import cache

from Publications.models import Publication

OPENALEX_WORKS = "https://api.openalex.org/works"
CROSSREF_WORKS = "https://api.crossref.org/works/"
DOI_RESOLVER = "https://doi.org/"
CONTACT = "contact@asphaltmine.org"
TIMEOUT = 8
WATCHED_CACHE_SECONDS = 86400
OPENALEX_FIELDS = "id,doi,title,publication_year,type,open_access,primary_location,referenced_works"
OPENALEX_ACCEPTED = {"article", "review", "book-chapter", "conference-paper"}
CROSSREF_ACCEPTED = {"journal-article", "proceedings-article", "book-chapter"}
RECORD_ACCEPTED = CROSSREF_ACCEPTED | {"article-journal", "paper-conference", "chapter"}
PREPRINT_PREFIXES = ("10.48550/", "10.2139/", "10.31219/", "10.21203/", "10.20944/", "10.22541/", "10.1101/")
KIND_NAMES = {"article": "journal article", "conference": "conference paper", "chapter": "book chapter"}


def _request(url, params=None, headers=None):
    merged = {"User-Agent": "AsphaltMine/1.0 (mailto:%s)" % CONTACT}
    if headers:
        merged.update(headers)
    try:
        response = requests.get(url, params=params, headers=merged, timeout=TIMEOUT)
    except requests.RequestException:
        return None, "error"
    if response.status_code == 404:
        return None, "missing"
    if response.status_code != 200:
        return None, "error"
    try:
        return response.json(), "ok"
    except ValueError:
        return None, "error"


def openalex_work(doi):
    return _request(OPENALEX_WORKS + "/doi:" + quote(doi, safe="/:()"), {"select": OPENALEX_FIELDS})


def crossref_work(doi):
    data, state = _request(CROSSREF_WORKS + quote(doi, safe="/:()"))
    return (data.get("message") if data else None), state


def doi_record(doi):
    return _request(DOI_RESOLVER + quote(doi, safe="/:()"), headers={"Accept": "application/vnd.citationstyles.csl+json"})


def watched_papers():
    dois = list(
        Publication.objects.filter(category__in=[Publication.FOUNDATION, Publication.MODELS], published=True)
        .values_list("doi", flat=True)
    )
    return [doi for doi in dois if not doi.startswith("10.0000/")]


def watched_categories():
    papers = Publication.objects.filter(category__in=[Publication.FOUNDATION, Publication.MODELS], published=True)
    return {paper.doi: paper.category for paper in papers if not paper.doi.startswith("10.0000/")}


def prediction_models_note(uses_models, result):
    if not uses_models:
        return None
    if not result["foundation_available"]:
        return "Prediction models cite AsphaltMine: not checked, no foundation paper is listed yet"
    if result["cites_foundation"]:
        return "Prediction models cite AsphaltMine: yes, the AsphaltMine foundation paper is cited"
    return "Prediction models cite AsphaltMine: no, the foundation paper is not cited (a website citation is not detected)"


def watched_openalex_ids():
    dois = watched_papers()
    key = "publications_watched_" + str(hash(tuple(sorted(dois))))
    cached = cache.get(key)
    if cached is not None:
        return cached
    if not dois:
        return {}
    data, state = _request(OPENALEX_WORKS, {"filter": "doi:" + "|".join(dois), "select": "id,doi", "per-page": 50})
    if state != "ok":
        return None
    found = {item["id"]: (item.get("doi") or "").replace("https://doi.org/", "").lower() for item in data.get("results", [])}
    cache.set(key, found, WATCHED_CACHE_SECONDS)
    return found


def normalize_issn(value):
    return re.sub(r"[^0-9Xx]", "", str(value or "")).upper()


@lru_cache(maxsize=4)
def _load_scopus_issns(path, modified):
    issns = set()
    with open(path, encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            for column in ("ISSN", "EISSN"):
                value = normalize_issn(row.get(column))
                if value:
                    issns.add(value)
    return frozenset(issns)


def scopus_sources_path():
    configured = getattr(settings, "SCOPUS_SOURCES_PATH", None)
    if configured:
        return configured
    candidate = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "scopus_sources.csv")
    return candidate if os.path.exists(candidate) else None


def scopus_indexed(issns, path=None):
    path = path or scopus_sources_path()
    if not path or not os.path.exists(path):
        return None
    known = _load_scopus_issns(path, os.path.getmtime(path))
    wanted = {normalize_issn(value) for value in issns if normalize_issn(value)}
    return bool(wanted & known)


def _first(value):
    if isinstance(value, list):
        return value[0] if value else ""
    return value or ""


def _year(data):
    parts = ((data.get("issued") or {}).get("date-parts") or [[None]])[0]
    return parts[0] if parts else None


def verify(doi, scopus_path=None):
    openalex, openalex_state = openalex_work(doi)
    crossref, crossref_state = crossref_work(doi)
    record, record_state = (None, "skipped")
    if not (openalex or crossref):
        record, record_state = doi_record(doi)

    states = {"OpenAlex": openalex_state, "Crossref": crossref_state, "DOI record": record_state}
    answered = [name for name, state in states.items() if state == "ok"]
    unavailable = [name for name, state in states.items() if state == "error"]

    source = ((openalex or {}).get("primary_location") or {}).get("source") or {}
    title = (openalex or {}).get("title") or _first((crossref or {}).get("title")) or _first((record or {}).get("title"))
    journal = source.get("display_name") or _first((crossref or {}).get("container-title")) or _first((record or {}).get("container-title"))
    year = (openalex or {}).get("publication_year") or (_year(crossref) if crossref else None) or (_year(record) if record else None)

    openalex_type = (openalex or {}).get("type") or ""
    crossref_type = (crossref or {}).get("type") or ""
    record_type = (record or {}).get("type") or ""
    accepted = not doi.startswith(PREPRINT_PREFIXES)
    if openalex_type and openalex_type not in OPENALEX_ACCEPTED:
        accepted = False
    if crossref_type and crossref_type not in CROSSREF_ACCEPTED:
        accepted = False
    if not openalex_type and not crossref_type and record_type and record_type not in RECORD_ACCEPTED:
        accepted = False
    detailed = crossref_type or record_type
    if detailed in ("book-chapter", "chapter"):
        kind = "chapter"
    elif detailed in ("proceedings-article", "paper-conference") or openalex_type == "conference-paper" or source.get("type") == "conference":
        kind = "conference"
    elif openalex_type == "book-chapter":
        kind = "chapter"
    else:
        kind = "article"

    issns = list(source.get("issn") or [])
    if source.get("issn_l"):
        issns.append(source["issn_l"])
    issns += list((crossref or {}).get("ISSN") or []) + list((record or {}).get("ISSN") or [])
    issns = sorted({normalize_issn(value) for value in issns if normalize_issn(value)})

    open_access = ""
    if openalex:
        open_access = "open" if (openalex.get("open_access") or {}).get("is_oa") else "closed"

    watched = watched_openalex_ids()
    categories = watched_categories()
    watched_dois = set(categories)
    foundation_dois = {doi_ for doi_, category in categories.items() if category == Publication.FOUNDATION}
    cites = {}
    for reference in (openalex or {}).get("referenced_works", []):
        if watched and reference in watched:
            cites[watched[reference]] = "OpenAlex"
    for reference in (crossref or {}).get("reference", []):
        reference_doi = str(reference.get("DOI", "")).lower()
        if reference_doi in watched_dois:
            cites[reference_doi] = "OpenAlex and Crossref" if reference_doi in cites else "Crossref"

    scopus = scopus_indexed(issns, scopus_path)
    found = bool(title)

    report = []
    if found:
        report.append("Publication found: yes (%s)" % ", ".join(answered))
        if accepted:
            report.append("Type: %s" % KIND_NAMES[kind])
            report.append("Published work: yes")
        else:
            report.append("Type: %s" % (openalex_type or crossref_type or record_type or "unknown"))
            report.append("Published work: no, only published journal articles, conference papers and book chapters are accepted")
        checked_sources = [name for name in ("OpenAlex", "Crossref") if states[name] == "ok"]
        if cites:
            titles = dict(Publication.objects.filter(doi__in=list(cites)).values_list("doi", "title"))
            report.append("Cites an AsphaltMine paper: yes")
            for cited, via in cites.items():
                role = "foundation paper" if categories.get(cited) == Publication.FOUNDATION else "prediction model paper"
                report.append("AsphaltMine paper cited (%s): %s (%s), found via %s" % (role, titles.get(cited, cited), cited, via))
        elif not checked_sources or watched is None:
            report.append("Cites an AsphaltMine paper: not checked, the citation databases could not be read")
        else:
            report.append("Cites an AsphaltMine paper: no (checked in %s)" % " and ".join(checked_sources))
        if scopus is None:
            report.append("Scopus: not checked, the Scopus list is not installed")
        elif scopus:
            report.append("Scopus: yes (ISSN %s found in the Scopus list)" % ", ".join(issns))
        elif issns:
            report.append("Scopus: no (ISSN %s not in the Scopus list)" % ", ".join(issns))
        else:
            report.append("Scopus: no (the publication has no ISSN to match)")
    elif unavailable:
        report.append("Publication found: could not be checked, %s did not answer" % ", ".join(unavailable))
    else:
        report.append("Publication found: no, the DOI is not known to %s" % ", ".join(name for name, state in states.items() if state == "missing"))

    return {
        "found": found,
        "unavailable": bool(unavailable) and not found,
        "title": title,
        "journal": journal,
        "year": year,
        "kind": kind,
        "accepted": accepted,
        "access": open_access,
        "issns": issns,
        "cites": cites,
        "cites_foundation": bool(set(cites) & foundation_dois),
        "foundation_available": bool(foundation_dois),
        "scopus": scopus,
        "sources": answered,
        "report": report,
    }
