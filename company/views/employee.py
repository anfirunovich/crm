from rest_framework import viewsets

from company.models.employee import Employee, Skill
from company.serializers.employee import EmployeeSerializer, SkillSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True).all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_active=True).all()