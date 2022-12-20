from rest_framework import viewsets

from crm.employee.models import Employee
from crm.employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()