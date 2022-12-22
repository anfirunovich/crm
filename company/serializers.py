from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'info',
            'tagline',
            'logo',
            'foundation_date',
            'location',
            'phone_number',
            'email',
            'id',
        )




