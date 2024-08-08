""" Site-wide template context processors for AsphaltMine.
"""
from django.conf import settings


def app_version(request):
    """Exposes settings.APP_VERSION to every template as APP_VERSION.

    Bump the version in one place (settings.py) instead of editing the
    footer HTML for every release.
    """
    return {"APP_VERSION": getattr(settings, "APP_VERSION", "")}


def write_access_request(request):
    user = getattr(request, "user", None)
    if not user or not user.is_authenticated:
        return {}
    from mdcs.views import has_write_access_request

    return {"write_access_requested": lambda: has_write_access_request(user)}
