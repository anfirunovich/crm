from rest_framework import serializers

from company.models import Company, Location


class CompanyModelSerializer(serializers.Serializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'info',
            'tagline',
            'logo',
            'since',
            'location',
            'phone_number',
            'email',
            'id',
        )


class LocationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'country',
            'city',
            'street',
            'house_number',
            'id',
        )

