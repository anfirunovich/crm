from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from company.models.employee import LanguageKnowledgeLevel, JobTitle
from company.models.language import Language
from company.models.company import Company

from company.serializers.employee import EmployeeSerializer, JobTitleAddEmployeeSerializer
from company.serializers.language import LanguageSerializer

from company.serializers.company import (
    RemoveEmployeeCompanySerializer,
    AddLocationToCompanySerializer,
    AddPartnerToCompanySerializer,
    CompanyRetrieveSerializer,
    CompanyCreateSerializer,
    CompanySerializer,
    EditEmployeeCompanySerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    default_serializer_class = CompanySerializer
    serializer_classes = {
        "list": CompanySerializer,
        "retrieve": CompanyRetrieveSerializer,
        "create": CompanyCreateSerializer,
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
        company = self.get_object()

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
        detail=True,
        url_path="add_employee",
        default_serializer_class=JobTitleAddEmployeeSerializer,
    )
    def add_employee_to_company(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        JobTitle.objects.create(
            company=company,
            employee=serializer.validated_data["employee"],
            job_title=serializer.validated_data["job_title"],
        )

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=('POST',),
        detail=True,
        url_path="add_location",
        default_serializer_class=AddLocationToCompanySerializer,
    )
    def add_location_to_company(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company.locations.add(serializer.validated_data["location"])

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=('POST',),
        detail=True,
        url_path="add_partner",
        default_serializer_class=AddPartnerToCompanySerializer,
    )
    def add_partner_to_company(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company.partners.add(serializer.validated_data["to_company"])

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=('POST',),
        detail=True,
        url_path="remove_employee",
        default_serializer_class=RemoveEmployeeCompanySerializer,
    )
    def remove_employee(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company.employees.remove(serializer.validated_data["employee"])

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=('POST',),
        detail=True,
        url_path="bulk_edit_employees",
        default_serializer_class=EditEmployeeCompanySerializer,
    )
    def bulk_edit_employees(self, request, pk=None):
        company = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["employees_ids_to_add"]:
            company.employees.add(*serializer.validated_data["employees_ids_to_add"])

        if serializer.validated_data["employees_ids_to_remove"]:
            company.employees.remove(*serializer.validated_data["employees_ids_to_remove"])

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)