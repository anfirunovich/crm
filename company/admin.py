from django.contrib import admin

from company.models.company import Company
from company.models.employee import Employee, Skill, JobTitle, LanguageKnowledgeLevel
from company.models.language import Language
from company.models.location import Location


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date',)
    list_filter = ('created_at',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('created_at',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('created_at',)


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('company', 'employee', 'company_id')


@admin.register(LanguageKnowledgeLevel)
class LanguageKnowledgeLevelAdmin(admin.ModelAdmin):
    list_display = ('employee', 'language', 'employee_id')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number',)
    list_filter = ('created_at',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'description',)