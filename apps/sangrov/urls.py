from django.urls import path

from apps.sangrov.views import CheckCodeView

urlpatterns = [
    path("check/", CheckCodeView.as_view(), name="check_code"),
]
