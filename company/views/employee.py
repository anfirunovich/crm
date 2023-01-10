from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from company.models.employee import Employee

from company.serializers.company import CompanySerializer
from company.serializers.employee import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

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




