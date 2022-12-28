from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from company.models.employee import Employee, LanguageKnowledgeLevel
from company.models.language import Language
from company.serializers.company import CompanySerializer, CompanyRetrieveSerializer
from company.serializers.employee import EmployeeSerializer

from company.models.company import Company
from company.serializers.language import LanguageSerializer


class CompanyViewSet(viewsets.ModelViewSet):

    default_serializer_class = CompanySerializer
    serializer_classes = {
        "list": CompanySerializer,
        "retrieve": CompanyRetrieveSerializer,
    }

    queryset = Company.objects.filter(is_active=True).all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(
        methods=('GET',),
        detail=True,
        url_path="employees",
        default_serializer_class=EmployeeSerializer,
    )
    def get_employees(self, request, pk=None):
          = self.get_object()

        serializer = self.get_serializer(company.employees.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=('GET',),
        detail=True,
        url_path="languages",
        default_serializer_class=LanguageSerializer,
    )
    def get_languages(self, request, pk=None):
        company = self.get_object()

        employees_ids = company.employees.values_list("id", flat=True).all()

        languages_ids = LanguageKnowledgeLevel.objects.filter(
            employee_id__in=employees_ids
        ).values_list("language_id", flat=True).all()

        serializer = self.get_serializer(
            Language.objects.filter(id__in=languages_ids).all(),
            many=True,
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=('GET',),
        detail=False,
        url_path="deleted_companies",
    )
    def get_deleted_companies(self, request):
        serializer = self.get_serializer(
            Company.objects.filter(is_active=False).all(),
            many=True,
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=('POST',),
        detail=False,
        url_path="add_employees",
        default_serializer_class=CompanySerializer,
    )
    def get_add_employees(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(Company.objects.add(employee_id=1).all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)