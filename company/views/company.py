from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from company.models.employee import Employee
from company.models.location import Location
from company.serializers.company import CompanySerializer, CompanyRetrieveSerializer
from company.serializers.employee import EmployeeSerializer

from company.models.company import Company


class CompanyViewSet(viewsets.ModelViewSet):

    employees_quantity = Employee.objects.annotate(num_employee=Count('id'))
    locations_quantity = Location.objects.annotate(num_location=Count('id'))

    default_serializer_class = CompanySerializer
    serializer_classes = {
        "list": CompanySerializer,
        "retrieve": CompanyRetrieveSerializer,
    }

    queryset = Company.objects.filter(is_active=True).all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_employees_quantity(self, obj):
        return obj.employee.employees_quantity

    def get_locations_quantity(self, obj):
        return obj.location.locations_quantity

    @action(
        methods=('GET',),
        detail=True,
        url_path="employees",
        default_serializer_class=EmployeeSerializer,
    )
    def get_employees(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(company.employees.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=('GET',),
        detail=True,
        url_path="employees",
        default_serializer_class=EmployeeSerializer,
    )
    def get_languages(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(company.employees.language.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
