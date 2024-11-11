from django.db import models

from apps.sangrov.models import AbstractBaseModel


class Sns(AbstractBaseModel):
    no = models.BigIntegerField(verbose_name="No",null=True, blank=True)
    delivery_date = models.CharField(max_length=255, verbose_name="Delivery Date",null=True, blank=True)
    customer_name = models.CharField(max_length=255, verbose_name="Customer Name",null=True, blank=True)
    material_number = models.CharField(max_length=255, verbose_name="Material Number",null=True, blank=True)
    material_description = models.CharField(max_length=255, verbose_name="Material Description",null=True, blank=True)
    shipped_quantity = models.CharField(max_length=255, verbose_name="Shipped Quantity",null=True, blank=True)
    serial_number = models.CharField(max_length=255, verbose_name="Serial Number",null=True, blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = "Sns"
        verbose_name_plural = "Sns"
        db_table = "sns"
        ordering = ["-created_at"]
