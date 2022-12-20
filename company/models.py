from django.db import models
from django_countries.fields import CountryField

from mixins.ModelMixin import CreatedAt, UpdatedAt, SoftDelete


class Company(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    location = CountryField(verbose_name="Location")

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"
