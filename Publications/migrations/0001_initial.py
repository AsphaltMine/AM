from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def seed_usage_labels(apps, schema_editor):
    PublicationUsage = apps.get_model("publications", "PublicationUsage")
    for order, name in enumerate(["Used data", "Used prediction models"], start=1):
        PublicationUsage.objects.get_or_create(name=name, defaults={"order": order})


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='Lower numbers come first.')),
            ],
            options={
                'verbose_name': 'usage label',
                'verbose_name_plural': 'usage labels',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PublicationSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('journal', models.CharField(blank=True, max_length=300)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('kind', models.CharField(blank=True, max_length=20)),
                ('access', models.CharField(blank=True, max_length=10)),
                ('cites', models.TextField(blank=True)),
                ('scopus', models.BooleanField(blank=True, null=True)),
                ('report', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reviewed_on', models.DateTimeField(blank=True, null=True)),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_publication_submissions', to=settings.AUTH_USER_MODEL)),
                ('usages', models.ManyToManyField(blank=True, related_name='submissions', to='publications.publicationusage')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publication_submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(help_text='Separate names with semicolons.', max_length=1000)),
                ('journal', models.CharField(help_text='Journal, conference or institution.', max_length=300)),
                ('published_on', models.DateField(help_text='Use the first day of the month if the day is unknown.')),
                ('volume', models.CharField(blank=True, max_length=20)),
                ('article_number', models.CharField(blank=True, max_length=40)),
                ('doi', models.CharField(error_messages={'unique': 'This paper is already listed in another entry or tab.'}, help_text='A paper can be listed only once, in a single tab.', max_length=200, unique=True)),
                ('abstract', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('foundation', 'AsphaltMine Foundation'), ('models', 'Asphalt Prediction Models'), ('studies', 'Studies Using AsphaltMine')], max_length=20)),
                ('model_name', models.CharField(blank=True, help_text='Only for Asphalt Prediction Models, for example Marshall Model.', max_length=60)),
                ('kind', models.CharField(choices=[('article', 'Journal article'), ('conference', 'Conference paper'), ('chapter', 'Book chapter')], default='article', max_length=20)),
                ('access', models.CharField(choices=[('open', 'Open access'), ('closed', 'Subscription')], default='closed', max_length=10)),
                ('published', models.BooleanField(default=True)),
                ('usages', models.ManyToManyField(blank=True, help_text='Only for Studies Using AsphaltMine.', related_name='publications', to='publications.publicationusage')),
            ],
            options={
                'ordering': ['-published_on', 'title'],
            },
        ),
        migrations.RunPython(seed_usage_labels, migrations.RunPython.noop),
    ]
