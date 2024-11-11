from django.db import models

from apps.shared.models import AbstractBaseModel


class Data(AbstractBaseModel):
    type = models.ForeignKey("Type", on_delete=models.CASCADE, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    material_code = models.CharField(max_length=255, null=True, blank=True)
    delivery_term = models.ForeignKey(
        "DeliveryTerm", on_delete=models.CASCADE, null=True, blank=True
    )
    warranty = models.BigIntegerField(null=True, blank=True)
    phase = models.ForeignKey("Phase", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(f"{self.type} - {self.model}")

    class Meta:
        verbose_name_plural = "Data"
        db_table = "data"
        ordering = ["created_at"]
