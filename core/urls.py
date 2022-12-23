from rest_framework.routers import DefaultRouter

from core.views import LocationViewSet


router = DefaultRouter()
router.register('locations', LocationViewSet, basename='location')

urlpatterns = router.urls
