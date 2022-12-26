from django.db import models


class Language(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name="Title of language",
        null=False,
        blank=False,
    )

    code = models.CharField(
        max_length=3,
        verbose_name="Code of language",
        null=False,
        blank=False,
    )

    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

