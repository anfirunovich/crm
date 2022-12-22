from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from company.serializers import CompanySerializer
from company.models import Company


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_active=True).all()



