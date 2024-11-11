from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.sangrov.models import Phase


@admin.register(Phase)
class PhaseAdmin(ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
