from rest_framework import viewsets

from core.models import Location
from core.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.all()