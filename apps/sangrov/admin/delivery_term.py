from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.sangrov.models import DeliveryTerm


@admin.register(DeliveryTerm)
class DeliveryTermAdmin(ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
