from django.db import migrations


def create_periodic_tasks(apps, schema_editor):
    CrontabSchedule = apps.get_model("django_celery_beat", "CrontabSchedule")
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")

    every_4_hours, _ = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="*/4",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
    )
    PeriodicTask.objects.get_or_create(
        name="cleanup-media-every-4-hours",
        defaults={
            "task": "mdcs.tasks.cleanup_media",
            "crontab": every_4_hours,
            "args": "[4]",
        },
    )

    hourly, _ = CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="*",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
    )
    PeriodicTask.objects.get_or_create(
        name="refresh-live-insights-overview-hourly",
        defaults={
            "task": "mdcs.tasks.refresh_live_insights_overview",
            "crontab": hourly,
        },
    )


def remove_periodic_tasks(apps, schema_editor):
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")
    PeriodicTask.objects.filter(
        name__in=[
            "cleanup-media-every-4-hours",
            "refresh-live-insights-overview-hourly",
        ]
    ).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("django_celery_beat", "__latest__"),
    ]

    operations = [
        migrations.RunPython(create_periodic_tasks, remove_periodic_tasks),
    ]
