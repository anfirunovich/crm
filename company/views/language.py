from rest_framework import viewsets
from rest_framework.decorators import action

from company.serializers.language import LanguageSerializer
from company.models.language import Language


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

