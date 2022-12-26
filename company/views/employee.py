from rest_framework import viewsets

from company.models.employee import Employee, Skill, JobTitle
from company.serializers.employee import EmployeeSerializer, SkillSerializer, JobTitleSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True).all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_active=True).all()


class JobTitleViewSet(viewsets.ModelViewSet):
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.all()
