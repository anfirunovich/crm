from django.db import models

from mixins.model_mixins import CreatedAt, UpdatedAt, SoftDelete

from core.validators import phone_number_validator
from core.models import Location


class Company(CreatedAt, UpdatedAt, SoftDelete):

    name = models.CharField(max_length=255, verbose_name="Name of company", unique=True, null=False, blank=False)
    info = models.TextField(verbose_name="Info about company", null=True, blank=True)
    tagline = models.CharField(max_length=255, verbose_name="Companies tagline", null=True, blank=True)
    logo = models.ImageField(verbose_name="Companies logo")
    foundation_date = models.DateField(verbose_name="Foundation date", null=True, blank=True)

    phone_number = models.CharField(
        max_length=13,
        verbose_name="Phone number",
        blank=False,
        null=False,
        validators=(phone_number_validator,),
    )

    email = models.EmailField(max_length=255, verbose_name="Email", unique=True, null=False, blank=False)

    locations = models.ManyToManyField(Location, null=True, blank=True)

    partners = models.ManyToManyField('self', null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}, {self.location}"
