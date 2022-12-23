from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from company.serializers.company import CompanySerializer
from company.models.company import Company


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_active=True).all()

