import logging

from django.contrib.auth.models import Group, Permission

from core_main_app.permissions import rights as main_rights

logger = logging.getLogger(__name__)

READ_ONLY_PERMISSIONS = [
    ("core_explore_example_app", "access_explore_example"),
    ("core_explore_example_app", "access_explore_example_data_structure"),
    ("core_explore_example_app", "delete_query"),
    ("core_explore_example_app", "save_query"),
    ("core_linked_records_app", "read_pid_settings"),
]


def init_permissions():
    try:
        read_only_group, _ = Group.objects.get_or_create(
            name=main_rights.READ_ONLY_GROUP
        )
        for app_label, codename in READ_ONLY_PERMISSIONS:
            try:
                permission = Permission.objects.get(
                    content_type__app_label=app_label, codename=codename
                )
                read_only_group.permissions.add(permission)
            except Permission.DoesNotExist:
                logger.warning(
                    "Permission %s.%s not found, skipping"
                    % (app_label, codename)
                )
    except Exception as exception:
        logger.error(
            "Impossible to init mdcs_home read_only permissions: %s"
            % str(exception)
        )
