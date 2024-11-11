from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("DATA"),
        "items": [
            {
                "title": _("SNs"),
                "icon": "database",
                "link": reverse_lazy("admin:sangrov_sns_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_sns"
                ),
            },
            {
                "title": _("Data"),
                "icon": "description",
                "link": reverse_lazy("admin:sangrov_data_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_data"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Additional"),
        "items": [
            {
                "title": _("Type"),
                "icon": "format_list_bulleted",
                "link": reverse_lazy("admin:sangrov_type_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_sns"
                ),
            },
            {
                "title": _("Delivery term"),
                "icon": "local_shipping",
                "link": reverse_lazy("admin:sangrov_deliveryterm_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_data"
                ),
            },
            {
                "title": _("No. of phases"),
                "icon": "tag",
                "link": reverse_lazy("admin:sangrov_phase_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_data"
                ),
            },
        ],
    },
]
