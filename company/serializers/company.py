from rest_framework import serializers

from company.models.company import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'name',
            'info',
            'tagline',
            'logo',
            'foundation_date',
            'locations',
            'phone_number',
            'email',
            'id',
        )