from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from company.serializers.language import LanguageSerializer
from company.models.language import Language


class LanguageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

