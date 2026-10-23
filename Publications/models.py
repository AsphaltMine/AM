from django.conf import settings
from django.db import models

DOI_PREFIXES = ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:")


def normalize_doi(value):
    value = value.strip().lower()
    for prefix in DOI_PREFIXES:
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value.strip()


class PublicationUsage(models.Model):
    name = models.CharField(max_length=80, unique=True)
    order = models.PositiveSmallIntegerField(default=0, help_text="Lower numbers come first.")

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "usage label"
        verbose_name_plural = "usage labels"

    def __str__(self):
        return self.name


class Publication(models.Model):
    FOUNDATION = "foundation"
    MODELS = "models"
    STUDIES = "studies"
    CATEGORY_CHOICES = [
        (FOUNDATION, "AsphaltMine Foundation"),
        (MODELS, "Asphalt Prediction Models"),
        (STUDIES, "Studies Using AsphaltMine"),
    ]
    KIND_CHOICES = [
        ("article", "Journal article"),
        ("conference", "Conference paper"),
        ("chapter", "Book chapter"),
    ]
    ACCESS_CHOICES = [
        ("open", "Open access"),
        ("closed", "Subscription"),
    ]

    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=1000, help_text="Separate names with semicolons.")
    journal = models.CharField(max_length=300, help_text="Journal, conference or institution.")
    published_on = models.DateField(help_text="Use the first day of the month if the day is unknown.")
    volume = models.CharField(max_length=20, blank=True)
    article_number = models.CharField(max_length=40, blank=True)
    doi = models.CharField(
        max_length=200,
        unique=True,
        help_text="A paper can be listed only once, in a single tab.",
        error_messages={"unique": "This paper is already listed in another entry or tab."},
    )
    abstract = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    model_name = models.CharField(
        max_length=60,
        blank=True,
        help_text="Only for Asphalt Prediction Models, for example Marshall Model.",
    )
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="article")
    usages = models.ManyToManyField(
        PublicationUsage,
        blank=True,
        related_name="publications",
        help_text="Only for Studies Using AsphaltMine.",
    )
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default="closed")
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_on", "title"]

    def __str__(self):
        return self.title

    def clean(self):
        self.doi = normalize_doi(self.doi)

    def save(self, *args, **kwargs):
        self.doi = normalize_doi(self.doi)
        super().save(*args, **kwargs)

    @property
    def url(self):
        return "https://doi.org/" + self.doi

    @property
    def shows_abstract(self):
        return bool(self.abstract) and self.access == "open"

    @property
    def year(self):
        return self.published_on.year

    @property
    def author_list(self):
        return [name.strip() for name in self.authors.split(";") if name.strip()]


class PublicationSubmission(models.Model):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="publication_submissions",
    )
    doi = models.CharField(max_length=200)
    usages = models.ManyToManyField(PublicationUsage, blank=True, related_name="submissions")
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    title = models.CharField(max_length=500, blank=True)
    journal = models.CharField(max_length=300, blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    kind = models.CharField(max_length=20, blank=True)
    access = models.CharField(max_length=10, blank=True)
    cites = models.TextField(blank=True)
    scopus = models.BooleanField(null=True, blank=True)
    report = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_publication_submissions",
    )
    reviewed_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.doi

    def save(self, *args, **kwargs):
        self.doi = normalize_doi(self.doi)
        super().save(*args, **kwargs)
