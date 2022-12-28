from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from company.models.company import Company
from company.models.employee import Employee, Skill
from company.serializers.company import CompanySerializer
from company.serializers.employee import EmployeeSerializer, SkillSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True).all()

    @action(
        methods=('GET',),
        detail=True,
        url_path="companies",
        serializer_class=CompanySerializer,
    )
    def get_companies_of_employee(self, request, pk=None):
        employee = self.get_object()

        serializer = self.get_serializer(employee.companies.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_active=True).all()


