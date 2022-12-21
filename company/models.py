from django.db import models
from django_countries.fields import CountryField

from mixins.model_mixins import CreatedAt, UpdatedAt, SoftDelete


class Location(CreatedAt, SoftDelete, UpdatedAt):

    country = CountryField(verbose_name="Location")
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.IntegerField()

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Company(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"
