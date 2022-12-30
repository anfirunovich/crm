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
            'partners',
            'phone_number',
            'email',
        )


class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'info',
            'tagline',
            'foundation_date',
            'phone_number',
            'email',
            'locations',
            'partners',
        )


class AddLocationToCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company.locations.through
        fields = (
            "id",
            "location",
        )


class AddPartnerToCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company.partners.through
        fields = (
            "id",
            "to_company",
        )
