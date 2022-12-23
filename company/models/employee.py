from django.db import models

from company.models.company import Company

from mixins.model_mixins import CreatedAt, UpdatedAt, SoftDelete


class Skill(CreatedAt, UpdatedAt, SoftDelete):
    title = models.CharField(max_length=255, verbose_name="Title", null=False, blank=False)
    description = models.CharField(max_length=255, verbose_name="Description", null=True, blank=True)

    def __str__(self):
        return self.title


class Employee(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=255, verbose_name="Employee name", null=False, blank=False)
    last_name = models.CharField(max_length=255, verbose_name="Employee lastname", null=False, blank=False)
    age = models.CharField(max_length=2, verbose_name="Employee age", null=False,  blank=False)

    LANGUAGE = [
        ('PY', 'Python'),
        ('JS', 'JavaScript'),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE, null=True, blank=True)
    skills = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=False)

    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.age}"
