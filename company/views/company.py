from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from company.serializers.company import CompanySerializer, CompanyRetrieveSerializer
from company.models.company import Company


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_classes = {
        "list": CompanySerializer,
        "retrieve": CompanyRetrieveSerializer,
    }
    queryset = Company.objects.filter(is_active=True).all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
