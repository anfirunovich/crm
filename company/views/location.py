from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from company.models.location import Location

from company.serializers.company import CompanySerializer
from company.serializers.location import LocationSerializer, LocationCompanySerializer


class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.filter(is_active=True).all()

    @action(
        methods=('GET',),
        detail=True,
        url_path="companies_of_location",
        serializer_class=LocationCompanySerializer,
    )
    def get_companies_of_location(self, request, pk=None):
        location = self.get_object()

        serializer = self.get_serializer(location.companies.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)