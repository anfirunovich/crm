from django.db import models

from core.model_mixins import CreatedAt, UpdatedAt, SoftDelete


class Skill(CreatedAt, UpdatedAt, SoftDelete):

    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=255,
        verbose_name="Description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title