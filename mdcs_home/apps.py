import sys

from django.apps import AppConfig


class MdcsHomeConfig(AppConfig):
    name = "mdcs_home"

    def ready(self):
        if "migrate" not in sys.argv:
            from mdcs_home.permissions import discover

            discover.init_permissions()
