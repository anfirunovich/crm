from rest_framework import serializers

from company.models.location import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'country',
            'city',
            'street',
            'house_number',
            'id',
        )