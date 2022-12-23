from django.contrib import admin

from company.models.company import Company
from company.models.employee import Employee
from company.models.location import Location


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date',)
    list_filter = ('created_at',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name',)
    list_filter = ('created_at',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number',)
    list_filter = ('created_at',)
