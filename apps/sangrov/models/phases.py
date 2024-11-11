from django.db import models

from apps.shared.models import AbstractBaseModel


class Phase(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Phases"
        ordering = ["name"]
        db_table = "phases"
