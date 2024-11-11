from django.db import models

from apps.shared.models import AbstractBaseModel


class DeliveryTerm(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Delivery Term"
        verbose_name_plural = "Delivery Terms"
        db_table = "delivery_terms"
