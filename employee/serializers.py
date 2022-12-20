from rest_framework import serializers

from crm.company.models import Company
from crm.employee import models
from crm.employee.models import Employee, Skills


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    age = serializers.CharField(max_length=2)

    language = serializers.CharField(max_length=2, choices=LANGUAGE)
    skills = serializers.ForeignKey(Skills, on_delete=models.PROTECT, null=True)

    company = serializers.ForeignKey(Company, on_delete=models.PROTECT, null=True)


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

