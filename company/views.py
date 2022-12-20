from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from crm.company.models import Company
from crm.company.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
