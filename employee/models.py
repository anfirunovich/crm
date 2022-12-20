from django.db import models

from company.models import Company

from mixins.ModelMixin import CreatedAt, UpdatedAt, SoftDelete


class Skill(CreatedAt, UpdatedAt, SoftDelete):
    title = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Employee(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=2)

    LANGUAGE = [
        ('PY', 'Python'),
        ('JS', 'JavaScript'),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE)
    skills = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)

    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.age}"

