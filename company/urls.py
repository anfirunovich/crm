from rest_framework.routers import DefaultRouter

from company.views.company import CompanyViewSet, CompanyListViewSet
from company.views.employee import EmployeeViewSet
from company.views.location import LocationViewSet


router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('locations', LocationViewSet, basename='location')


urlpatterns = router.urls
