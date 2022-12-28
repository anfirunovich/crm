from django.db.models import Count

from rest_framework import serializers

from company.models.company import Company
from company.models.employee import Employee
from company.models.location import Location
from company.serializers.location import LocationSerializer


class CompanySerializer(serializers.ModelSerializer):

    employees_quantity = serializers.SerializerMethodField()
    locations_quantity = serializers.SerializerMethodField()

    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'locations',
            'employees_quantity',
            'locations_quantity',
        )

    def get_employees_quantity(self, obj):
        return obj.employees.count()

    def get_locations_quantity(self, obj):
        return obj.locations.count()


class CompanyRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'info',
            'tagline',
            'logo',
            'foundation_date',
            'locations',
            'phone_number',
            'email',
        )