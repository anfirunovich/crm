from rest_framework import serializers

from employee.models import Employee, Skill


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'name',
            'last_name',
            'age',
            'language',
            'skills',
            'company',
            'id',
        )


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            'title',
            'describe',
            'id',
        )
