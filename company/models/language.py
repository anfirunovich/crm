from django.db import models


class Language(models.Model):
    title = models.CharField(
        max_length=20,
        null=False,
        blank=True,
    )

    code = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=255,
        verbose_name="Description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

