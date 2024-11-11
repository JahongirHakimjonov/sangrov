from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import DropdownFilter

from apps.sangrov.models import DeliveryTerm, Phase, Type, Data


class DeliveryTermFilter(DropdownFilter):
    title = _("Delivery Term")
    parameter_name = "delivery_term"

    def lookups(self, request, model_admin):
        delivery_terms = DeliveryTerm.objects.all()
        return [(delivery_term.id, delivery_term.name) for delivery_term in delivery_terms]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(delivery_term_id__id=self.value())
        return queryset


class PhaseFilter(DropdownFilter):
    title = _("No. of phases")
    parameter_name = "phase"

    def lookups(self, request, model_admin):
        phases = Phase.objects.all()
        return [(phase.id, phase.name) for phase in phases]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(phase_id__id=self.value())
        return queryset


class TypeFilter(DropdownFilter):
    title = _("Type")
    parameter_name = "type"

    def lookups(self, request, model_admin):
        types = Type.objects.all()
        return [(type.id, type.name) for type in types]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(type_id__id=self.value())
        return queryset


class WarrantyFilter(DropdownFilter):
    title = _("Warranty period")
    parameter_name = "warranty"

    def lookups(self, request, model_admin):
        datas = Data.objects.values_list('warranty', flat=True).distinct()
        return [(data, data) for data in datas]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(warranty=self.value())
        return queryset