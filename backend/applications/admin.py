from django.contrib import admin

from applications.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "student",
        "job",
        "status",
        "applied_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "student__email",
        "job__title",
    )