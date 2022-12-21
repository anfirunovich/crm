from django.core.validators import RegexValidator

from django.db import models

from django_countries.fields import CountryField

from mixins.model_mixins import CreatedAt, UpdatedAt, SoftDelete


class Location(CreatedAt, SoftDelete, UpdatedAt):

    country = CountryField(verbose_name="Country of company", null=False, blank=False)
    city = models.CharField(max_length=255, verbose_name="City of company", null=False, blank=False)
    street = models.CharField(max_length=255, verbose_name="Street", null=False, blank=False)
    house_number = models.PositiveSmallIntegerField(verbose_name="House number", null=False, blank=False)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Company(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(max_length=255, verbose_name="Name of company", null=False, blank=False)
    info = models.TextField(verbose_name="Info about company", null=True, blank=True)
    tagline = models.CharField(max_length=255, verbose_name="Tagline", null=True, blank=True)
    logo = models.ImageField()
    since = models.DateField(verbose_name="Since", null=True, blank=True)

    phone_number = models.CharField(
        max_length=13,
        verbose_name="Phone number",
        blank=True,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^\+375 \((29|44|33)\) [0-9]{3}-[0-9]{2}-[0-9]{2}$",

            ),
        ],
    )
    email = models.EmailField(max_length=255, verbose_name="Email", unique=True)

    locations = models.ManyToManyField(Location, null=True, blank=True)

    partners = models.ManyToManyField('Company', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"
