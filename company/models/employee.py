from django.db import models

from company.models.company import Company
from company.models.language import Language

from core.model_mixins import CreatedAt, UpdatedAt, SoftDelete
from core.enums.employee_enum import SexEnum, SizeEnum, LevelEnum
from core.validators import phone_number_validator


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


class Employee(CreatedAt, UpdatedAt, SoftDelete):

    first_name = models.CharField(
        max_length=255,
        verbose_name="Employee name",
        null=False,
        blank=False,
    )

    middle_name = models.CharField(
        max_length=255,
        verbose_name="Employee middle name",
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=255,
        verbose_name="Employee lastname",
        null=False,
        blank=False
    )

    age = models.CharField(
        max_length=2,
        verbose_name="Employee age",
        null=False,
        blank=False
    )

    sex = models.CharField(
        max_length=255,
        choices=SexEnum.choices(),
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        blank=True,
        null=True,
        validators=(phone_number_validator,),
    )

    clothing_size = models.CharField(
        max_length=1,
        choices=SizeEnum.choices(),
        blank=True,
        null=True,
    )

    languages = models.ManyToManyField(
        Language,
        through='LanguageKnowledgeLevel',
        through_fields=('employee', 'language'),
        related_name="employees",
        related_query_name="employees",
        null=False,
        blank=False,
    )

    skills = models.ManyToManyField(
        Skill,
        related_name="skills",
        related_query_name="skill",
        blank=True,
    )

    companies = models.ManyToManyField(
        Company,
        through='JobTitle',
        through_fields=('employee', 'company'),
        related_name="employees",
        related_query_name="employee",
        blank=False,
    )

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

        ordering = ("first_name", "last_name", "middle_name",)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}, {self.age}"


class JobTitle(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Job title in company",
        null=False,
        blank=False,
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee's job title",
        null=False,
        blank=False,
    )

    job_title = models.CharField(
        max_length=255,
        verbose_name="Job title",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "JobTitle"
        verbose_name_plural = "JobTitles"

        ordering = ("company_id", "employee_id",)

        constraints = (
            models.UniqueConstraint(
                fields=(
                    "company_id",
                    "employee_id",
                ),
                name="unique_job_title",
            ),
        )


class LanguageKnowledgeLevel(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee",
        null=False,
        blank=False,
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        verbose_name="Employee's language",
        null=False,
        blank=False,
    )

    knowledge_level = models.CharField(
        max_length=255,
        choices=LevelEnum.choices(),
        verbose_name="Employee's knowledge level",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "LanguageKnowledgeLevel"
        verbose_name_plural = "LanguagesKnowledgeLevels"

        ordering = ("employee_id", "language_id",)

        constraints = (
            models.UniqueConstraint(
                fields=(
                    "employee_id",
                    "language_id",
                ),
                name="unique_knowledge",
            ),
        )