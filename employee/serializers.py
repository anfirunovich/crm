from rest_framework import serializers

from employee.models import Employee, Skill


class EmployeeSerializer(serializers.Serializer):

    class Meta:
        model = Employee
        fields = ('name', 'last_name', 'age', 'language', 'skills', 'company', 'id',)


class SkillSerializer(serializers.Serializer):

    class Meta:
        model = Skill
        fields = ('title', 'describe', 'id',)
