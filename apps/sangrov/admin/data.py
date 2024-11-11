from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.decorators import display

from apps.sangrov.filters import DeliveryTermFilter, PhaseFilter, TypeFilter, WarrantyFilter
from apps.sangrov.models import Data


@admin.register(Data)
class DataAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = (
        "id",
        "type_with_color",
        "phase_with_color",
        "model_with_color",
        "material_with_color",
        "delivery_with_color",
        "warranty_with_color",
        "created_at",
        "is_active",
    )
    list_filter = (
        DeliveryTermFilter,
        PhaseFilter,
        TypeFilter,
        WarrantyFilter,
        "is_active",
    )
    search_fields = (
        "type__name",
        "phase__name",
        "model",
        "material_code",
        "delivery_term__name",
        "warranty",
    )
    autocomplete_fields = (
        "type",
        "phase",
        "delivery_term",
    )
    compressed_fields = True
    list_filter_submit = True
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "type",
                    "phase",
                    "delivery_term",
                    "model",
                    "material_code",
                    "warranty",
                    "is_active",
                )
            },
        ),
    )

    @display(description=_("Type"), label=True)
    def type_with_color(self, obj):
        return obj.type.name if obj.type else _("No type")

    @display(description=_("No. of phases"), label=True)
    def phase_with_color(self, obj):
        return obj.phase.name if obj.phase else _("No phases")

    @display(description=_("Model"), label=True)
    def model_with_color(self, obj):
        return obj.model if obj.model else _("No model")

    @display(description=_("Material code"), label=True)
    def material_with_color(self, obj):
        return obj.material_code if obj.material_code else _("No material code")

    @display(description=_("Delivery term"), label=True)
    def delivery_with_color(self, obj):
        return obj.delivery_term.name if obj.delivery_term else _("No delivery term")

    @display(description=_("Warranty Period"), label=True)
    def warranty_with_color(self, obj):
        return obj.warranty if obj.warranty else _("No warranty")
