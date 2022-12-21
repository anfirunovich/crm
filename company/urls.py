from rest_framework.routers import DefaultRouter

from company.views import CompanyViewSet, LocationViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('locations', LocationViewSet, basename='location')

urlpatterns = router.urls
