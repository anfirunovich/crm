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


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
        )


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    partners = PartnerSerializer(many=True)

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


class RemoveEmployeeCompanySerializer(serializers.Serializer):
    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(is_active=True).all(),
    )


class EditEmployeeCompanySerializer(serializers.Serializer):

    employees_ids_to_add = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=True,
        required=False,  # делает поле необязательным для ввода
        allow_null=True,  # разрешает передавать null (None) в качестве значения этого поля
    )

    employees_ids_to_remove = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=True,
        required=False,
        allow_null=True,
    )

    def validate_employees_ids_to_add(self, value):
        if value and Employee.objects.filter(is_active=True, id__in=value).count() != len(value):
            raise serializers.ValidationError(
                {
                    "reason": "Not all submitted ids actually persists in database",
                }
            )

        return value

    def validate_employees_ids_to_remove(self, value):
        if value and Employee.objects.filter(is_active=True, id__in=value).count() != len(value):
            raise serializers.ValidationError(
                {
                    "reason": "Not all submitted ids actually persists in database",
                }
            )

        return value

    def validate(self, data):
        if set(data["employees_ids_to_add"]) & set(data["employees_ids_to_remove"]):
            raise serializers.ValidationError(
                {
                    "reason": "Values must not be repeated in `employees_ids_to_add` and `employees_ids_to_remove`",
                }
            )

        return data
