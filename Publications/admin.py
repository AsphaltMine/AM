import re
from urllib.parse import quote

from django.contrib import admin, messages
from django.utils import timezone
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

from Publications.models import Publication, PublicationSubmission, PublicationUsage


@admin.register(PublicationUsage)
class PublicationUsageAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    ordering = ("order", "name")


@admin.register(PublicationSubmission)
class PublicationSubmissionAdmin(admin.ModelAdmin):
    list_display = ("doi", "open_publication", "title", "user", "usage_labels", "status", "cites_ours", "cited_titles", "scopus", "access", "already_listed", "created", "reviewed_by")
    list_filter = ("status", "scopus", "kind", "access")
    list_editable = ("status",)
    search_fields = ("doi", "user__username", "user__email", "note")
    readonly_fields = ("created", "report", "title", "journal", "year", "kind", "access", "cited_papers", "scopus", "doi_link", "user", "note", "report_display", "reviewed_by", "reviewed_on")
    filter_horizontal = ("usages",)
    ordering = ("-created",)
    fieldsets = (
        (None, {"fields": ("doi_link", "user", "usages", "note", "status", "created", "reviewed_by", "reviewed_on")}),
        ("Automatic check", {"fields": ("report_display", "title", "journal", "year", "kind", "access", "cited_papers", "scopus")}),
    )

    actions = ["publish_selected"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user").prefetch_related("usages")

    def _publish(self, request, submission):
        from Publications.publishing import publish_submission

        publication, text = publish_submission(submission)
        if publication:
            self.message_user(request, text, messages.SUCCESS)
        else:
            self.message_user(request, "%s: %s" % (submission.doi, text), messages.ERROR)
        return publication

    def save_model(self, request, obj, form, change):
        previous = None
        if change:
            previous = PublicationSubmission.objects.filter(pk=obj.pk).values_list("status", flat=True).first()
        if change and previous != obj.status:
            if obj.status == PublicationSubmission.PENDING:
                obj.reviewed_by = None
                obj.reviewed_on = None
            else:
                obj.reviewed_by = request.user
                obj.reviewed_on = timezone.now()
        super().save_model(request, obj, form, change)
        if obj.status == PublicationSubmission.APPROVED and previous != PublicationSubmission.APPROVED:
            if not self._publish(request, obj) and not Publication.objects.filter(doi=obj.doi).exists():
                obj.status = PublicationSubmission.PENDING
                obj.reviewed_by = None
                obj.reviewed_on = None
                obj.save(update_fields=["status", "reviewed_by", "reviewed_on"])

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        submission = form.instance
        if submission.status == PublicationSubmission.APPROVED:
            publication = Publication.objects.filter(doi=submission.doi).first()
            if publication:
                publication.usages.set(submission.usages.all())

    @admin.action(description="Publish the selected approved submissions")
    def publish_selected(self, request, queryset):
        for submission in queryset.filter(status=PublicationSubmission.APPROVED):
            self._publish(request, submission)

    def usage_labels(self, obj):
        return ", ".join(usage.name for usage in obj.usages.all())

    def report_display(self, obj):
        blocks = []
        for line in self._report_lines(obj.report):
            label, _, value = line.partition(": ")
            lowered = value.lower()
            for cited_doi, cited_title in self._cited_titles(obj).items():
                if cited_title not in value:
                    value = value.replace(cited_doi, "%s (%s)" % (cited_title, cited_doi))
            if re.match(r"^yes\b", lowered):
                mark, color = "&#10004;", "#2f8e5a"
            elif re.match(r"^no\b", lowered):
                mark, color = "&#10008;", "#b34040"
            elif lowered.startswith(("not checked", "could not")):
                mark, color = "&#9679;", "#8a97a3"
            else:
                mark, color = "", "#24323f"
            blocks.append(format_html(
                '<div style="margin:0 0 14px;line-height:1.5"><strong>{}</strong><br><span style="color:{}">{} {}</span></div>',
                label, color, mark_safe(mark), value,
            ))
        return format_html_join("", "{}", ((block,) for block in blocks)) if blocks else "-"

    report_display.short_description = "Report"

    def _report_lines(self, report):
        lines = []
        for line in report.splitlines():
            typed = re.match(r"^(Type: .+?)\. (Published work: .+)$", line)
            if typed:
                lines += [typed.group(1), typed.group(2)]
                continue
            cited = re.match(r"^Cites an AsphaltMine paper: yes \((.+)\)$", line)
            if cited:
                lines.append("Cites an AsphaltMine paper: yes")
                for part in cited.group(1).split("; "):
                    doi, _, via = part.partition(" via ")
                    lines.append("AsphaltMine paper cited: %s, found via %s" % (doi, via))
                continue
            lines.append(line)
        return lines

    def _cited_titles(self, obj):
        dois = [line.strip() for line in obj.cites.splitlines() if line.strip()]
        return dict(Publication.objects.filter(doi__in=dois).values_list("doi", "title"))

    def cited_papers(self, obj):
        dois = [line.strip() for line in obj.cites.splitlines() if line.strip()]
        if not dois:
            return "-"
        titles = self._cited_titles(obj)
        return format_html_join(
            "",
            '<div style="margin:0 0 10px;line-height:1.5"><a href="https://doi.org/{}" target="_blank" rel="noopener noreferrer">{}</a><br><span style="color:#6b7c8a">{}</span></div>',
            ((quote(doi, safe="/:()"), titles.get(doi, doi), doi) for doi in dois),
        )

    cited_papers.short_description = "AsphaltMine papers cited"

    def cited_titles(self, obj):
        titles = self._cited_titles(obj)
        names = [(titles.get(line.strip(), line.strip())) for line in obj.cites.splitlines() if line.strip()]
        return "; ".join(name if len(name) <= 60 else name[:57] + "..." for name in names) or "-"

    cited_titles.short_description = "Cited paper"

    def doi_link(self, obj):
        return format_html('<a href="https://doi.org/{}" target="_blank" rel="noopener noreferrer">{}</a>', quote(obj.doi, safe="/:()"), obj.doi)

    doi_link.short_description = "DOI"

    def open_publication(self, obj):
        return format_html('<a href="https://doi.org/{}" target="_blank" rel="noopener noreferrer">Open</a>', quote(obj.doi, safe="/:()"))

    open_publication.short_description = "Publication"

    def cites_ours(self, obj):
        return bool(obj.cites.strip())

    cites_ours.boolean = True
    cites_ours.short_description = "Cites AsphaltMine"

    def already_listed(self, obj):
        return Publication.objects.filter(doi=obj.doi).exists()

    already_listed.boolean = True
    already_listed.short_description = "Already listed"


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "model_name", "kind", "published_on", "usage_labels", "access", "published")
    list_filter = ("category", "kind", "usages", "access", "published")
    list_editable = ("published",)
    search_fields = ("title", "authors", "journal", "doi")
    ordering = ("-published_on", "title")
    filter_horizontal = ("usages",)
    fieldsets = (
        (None, {"fields": ("title", "authors", "journal", "published_on", "volume", "article_number", "doi")}),
        ("Abstract", {"fields": ("abstract",)}),
        ("Placement", {"fields": ("category", "model_name", "kind", "usages", "access", "published")}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("usages")

    def usage_labels(self, obj):
        return ", ".join(usage.name for usage in obj.usages.all())
