from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from company.models import Company, Location
from company.serializers import CompanySerializer, LocationSerializer


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.all()

