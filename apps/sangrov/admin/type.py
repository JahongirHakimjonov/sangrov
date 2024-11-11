from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.sangrov.models import Type


@admin.register(Type)
class TypeAdmin(ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
