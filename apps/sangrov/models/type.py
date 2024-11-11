from django.db import models

from apps.shared.models import AbstractBaseModel


class Type(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types"
        ordering = ["name"]
        db_table = "types"
