from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin

from apps.sangrov.models import Sns


@admin.register(Sns)
class SnsAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = (
        "no",
        "delivery_date",
        "customer_name",
        "material_number",
        "material_description",
        "shipped_quantity",
        "serial_number",
        "created_at",
        "is_active",
    )
    search_fields = (
        "no",
        "delivery_date",
        "customer_name",
        "material_number",
        "material_description",
        "shipped_quantity",
        "serial_number",
    )
    list_filter = ("is_active",)
    list_filter_submit = True
