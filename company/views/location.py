from rest_framework import viewsets

from company.models.location import Location
from company.serializers.location import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.all()