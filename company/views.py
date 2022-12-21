from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from company.models import Company
from company.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
