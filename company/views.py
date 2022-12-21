from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from company.models import Company, Location
from company.serializers import CompanyModelSerializer, LocationModelSerializer


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationModelSerializer
    queryset = Location.objects.all()

