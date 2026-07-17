""" Admin urls
"""

from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered

from core_main_app.utils.admin_site.model_admin_class import (
    register_simple_history_models,
)
from django.conf import settings

DJANGO_SIMPLE_HISTORY_MODELS = getattr(
    settings, "DJANGO_SIMPLE_HISTORY_MODELS", None
)
register_simple_history_models(DJANGO_SIMPLE_HISTORY_MODELS)

# Unused admin models
_UNUSED_ADMIN_MODELS = [
    ("sites", "Site"),
    ("oauth2_provider", "Application"),
    ("oauth2_provider", "AccessToken"),
    ("oauth2_provider", "RefreshToken"),
    ("oauth2_provider", "Grant"),
    ("oauth2_provider", "IDToken"),
    ("core_composer_app", "Type"),
    ("core_composer_app", "TypeVersionManager"),
    ("core_composer_app", "Bucket"),
    ("core_explore_example_app", "ExploreDataStructure"),
    ("core_explore_example_app", "PersistentQueryExample"),
    ("core_explore_example_app", "SavedQuery"),
    ("core_federated_search_app", "Instance"),
    ("core_linked_records_app", "LocalId"),
    ("core_linked_records_app", "PidPath"),
    ("core_linked_records_app", "PidSettings"),
    ("core_parser_app", "DataStructure"),
    ("core_parser_app", "DataStructureElement"),
    ("core_parser_app", "Module"),
]

for _app_label, _model_name in _UNUSED_ADMIN_MODELS:
    try:
        admin.site.unregister(django_apps.get_model(_app_label, _model_name))
    except (LookupError, NotRegistered):
        pass
