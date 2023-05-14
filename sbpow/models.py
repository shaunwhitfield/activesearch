from django.db import models
from django.utils import timezone

class PlaceOfWorship(models.Model):
    name = models.CharField("Name", max_length=200)
    religion = models.CharField("Religion", max_length=200)
    denomination = models.CharField("Denomination", max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    address1 = models.CharField("Address line 1", max_length=1024, null=True, blank=True)
    address2 = models.CharField("Address line 2", max_length=1024, null=True, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12, null=True, blank=True)
    city = models.CharField("City", max_length=1024, null=True, blank=True)
    state = models.CharField("State", max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Places of Worship"