from rest_framework import viewsets

from employee.models import Employee, Skill
from employee.serializers import EmployeeModelSerializer, SkillModelSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeModelSerializer
    queryset = Employee.objects.all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillModelSerializer
    queryset = Skill.objects.all()