import re
from datetime import date
from urllib.parse import quote

from Publications import verify
from Publications.models import Publication

TAGS = re.compile(r"<[^>]+>")


def _abstract(openalex, crossref):
    index = (openalex or {}).get("abstract_inverted_index")
    if index:
        placed = sorted((position, word) for word, positions in index.items() for position in positions)
        return " ".join(word for _, word in placed)
    if crossref and crossref.get("abstract"):
        return re.sub(r"\s+", " ", TAGS.sub(" ", crossref["abstract"])).strip()
    return ""


def _date(openalex, crossref):
    parts = (((crossref or {}).get("issued") or {}).get("date-parts") or [[None]])[0]
    if parts and parts[0]:
        return date(parts[0], parts[1] if len(parts) > 1 and parts[1] else 1, parts[2] if len(parts) > 2 and parts[2] else 1)
    value = (openalex or {}).get("publication_date")
    if value:
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    year = (openalex or {}).get("publication_year")
    return date(year, 1, 1) if year else None


def fetch_details(doi):
    openalex, _ = verify._request(
        verify.OPENALEX_WORKS + "/doi:" + quote(doi, safe="/:()"),
        {"select": "title,publication_year,publication_date,authorships,abstract_inverted_index,biblio"},
    )
    crossref, _ = verify.crossref_work(doi)
    authors = [
        ("%s %s" % (person.get("given", ""), person.get("family", ""))).strip()
        for person in (crossref or {}).get("author", [])
        if person.get("family")
    ]
    if not authors:
        authors = [
            item["author"]["display_name"]
            for item in (openalex or {}).get("authorships", [])
            if (item.get("author") or {}).get("display_name")
        ]
    biblio = (openalex or {}).get("biblio") or {}
    return {
        "authors": authors,
        "date": _date(openalex, crossref),
        "volume": str((crossref or {}).get("volume") or biblio.get("volume") or ""),
        "article_number": str((crossref or {}).get("article-number") or biblio.get("first_page") or ""),
        "abstract": _abstract(openalex, crossref),
    }


def publish_submission(submission):
    doi = submission.doi
    if Publication.objects.filter(doi=doi).exists():
        return None, "This publication is already listed."
    details = fetch_details(doi)
    if not submission.title or not details["authors"] or not details["date"]:
        return None, "The details of this publication could not be read. Add it by hand in Publications."
    publication = Publication.objects.create(
        title=submission.title[:500],
        authors="; ".join(details["authors"])[:1000],
        journal=(submission.journal or "")[:300],
        published_on=details["date"],
        volume=details["volume"][:20],
        article_number=details["article_number"][:40],
        doi=doi,
        abstract=details["abstract"] if submission.access == "open" else "",
        category=Publication.STUDIES,
        kind=submission.kind or "article",
        access=submission.access or "closed",
        published=True,
    )
    publication.usages.set(submission.usages.all())
    return publication, "Published on the Studies tab: %s" % publication.title
