from django import template

from Publications import citation

register = template.Library()


@register.filter
def reference(paper):
    return citation.format_reference(paper)


@register.filter
def ris(paper):
    return citation.ris_entry(paper) + "\r\n"


@register.filter
def bibtex(paper):
    return citation.bibtex_entry(paper) + "\n"
