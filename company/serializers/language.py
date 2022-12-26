from rest_framework import serializers

from company.models.language import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = (
            'id',
            'title',
            'code',
            'description',
        )
