from django.db import models

from django_countries.fields import CountryField

from core.model_mixins import CreatedAt, UpdatedAt, SoftDelete


class Location(CreatedAt, SoftDelete, UpdatedAt):

    country = CountryField(
        verbose_name="Location's country",
        null=False,
        blank=False
    )

    city = models.CharField(
        max_length=255,
        verbose_name="Location's city",
        null=False,
        blank=False
    )

    street = models.CharField(
        max_length=255,
        verbose_name="Street",
        null=False,
        blank=False
    )

    house_number = models.PositiveSmallIntegerField(
        verbose_name="House number",
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

        ordering = ("country", "city",)
