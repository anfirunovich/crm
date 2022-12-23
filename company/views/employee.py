from rest_framework import viewsets

from company.models.employee import Employee, Skill
from company.serializers.employee import EmployeeSerializer, SkillSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()