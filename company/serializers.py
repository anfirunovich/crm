from rest_framework import serializers

from company.models import Company, Location


class CompanySerializer(serializers.Serializer):

    class Meta:
        model = Company
        fields = ('name', 'info', 'location', 'id',)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('country', 'city', 'street', 'house_number', 'id')

