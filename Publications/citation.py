import re

from Publications.models import Publication

CITE_REQUEST = "Please cite this paper when using AsphaltMine."
PUBLICATIONS_PATH = "/publications/"


def format_reference(paper):
    reference = "%s (%s). %s. %s" % (", ".join(paper.author_list), paper.year, paper.title.rstrip("."), paper.journal)
    if paper.volume:
        reference += ", " + paper.volume
    if paper.article_number:
        reference += ", " + paper.article_number
    return reference + ". " + paper.url


RIS_TYPES = {"article": "JOUR", "conference": "CPAPER", "chapter": "CHAP"}
BIBTEX_TYPES = {"article": "article", "conference": "inproceedings", "chapter": "incollection"}
BIBTEX_VENUE = {"article": "journal", "conference": "booktitle", "chapter": "booktitle"}
BIBTEX_ESCAPES = {"&": "\\&", "%": "\\%", "$": "\\$", "#": "\\#", "_": "\\_"}


def split_name(name):
    if "," in name:
        return name.strip()
    parts = name.split()
    if len(parts) < 2:
        return name.strip()
    return "%s, %s" % (parts[-1], " ".join(parts[:-1]))


def page_range(value):
    match = re.match(r"^(\d+)\s*[-\u2013]\s*(\d+)$", value.strip())
    return match.groups() if match else None


def ris_entry(paper):
    lines = ["TY  - " + RIS_TYPES.get(paper.kind, "JOUR")]
    lines += ["AU  - " + split_name(name) for name in paper.author_list]
    lines += ["TI  - " + paper.title, "T2  - " + paper.journal, "PY  - " + str(paper.year)]
    if paper.volume:
        lines.append("VL  - " + paper.volume)
    pages = page_range(paper.article_number)
    if pages:
        lines += ["SP  - " + pages[0], "EP  - " + pages[1]]
    elif paper.article_number:
        lines.append("C7  - " + paper.article_number)
    lines += ["DO  - " + paper.doi, "UR  - " + paper.url, "ER  - "]
    return "\r\n".join(lines)


def bibtex_escape(value):
    for character, replacement in BIBTEX_ESCAPES.items():
        value = value.replace(character, replacement)
    return value


def bibtex_key(paper):
    names = paper.author_list
    surname = split_name(names[0]).split(",")[0] if names else "paper"
    word = paper.title.split()[0] if paper.title.split() else ""
    return "".join(ch for ch in (surname + str(paper.year) + word).lower() if ch.isalnum())


def bibtex_entry(paper):
    kind = BIBTEX_TYPES.get(paper.kind, "article")
    fields = [
        ("author", " and ".join(split_name(name) for name in paper.author_list)),
        ("title", "{" + bibtex_escape(paper.title) + "}"),
        (BIBTEX_VENUE.get(paper.kind, "journal"), bibtex_escape(paper.journal)),
        ("year", str(paper.year)),
    ]
    if paper.volume:
        fields.append(("volume", paper.volume))
    if paper.article_number:
        pages = page_range(paper.article_number)
        fields.append(("pages", "--".join(pages) if pages else paper.article_number))
    fields += [("doi", paper.doi), ("url", paper.url)]
    body = ",\n".join("  %s = {%s}" % (name, value) for name, value in fields)
    return "@%s{%s,\n%s\n}" % (kind, bibtex_key(paper), body)


def references(category):
    papers = Publication.objects.filter(category=category, published=True)
    return [format_reference(paper) for paper in papers]
