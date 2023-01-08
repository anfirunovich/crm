from django.db import models

from django.conf import settings

from core.model_mixins import CreatedAt, UpdatedAt, SoftDelete
from core.validators import phone_number_validator

from company.models.location import Location


class Company(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(
        max_length=255,
        verbose_name="Name of company",
        unique=True,
        null=False,
        blank=False,
    )

    info = models.TextField(verbose_name="Info about company", null=True, blank=True,)
    tagline = models.CharField(
        max_length=255,
        verbose_name="Companies tagline",
        null=True,
        blank=True
    )

    logo = models.ImageField(verbose_name="Companies logo", null=True, blank=True)
    foundation_date = models.DateField(verbose_name="Foundation date", null=True, blank=True)

    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        null=False,
        blank=False,
        validators=(phone_number_validator,),
    )

    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        unique=True,
        null=False,
        blank=False
    )

    locations = models.ManyToManyField(
        Location,
        related_name="companies",
        related_query_name="company",
        blank=False,
    )

    partners = models.ManyToManyField('self', blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

        ordering = ("name",)

    def __str__(self):
        return f"{self.name}, {self.email}"
