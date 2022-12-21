from rest_framework.routers import DefaultRouter

from employee.views import EmployeeViewSet, SkillViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('skills', SkillViewSet, basename='skill')

urlpatterns = router.urls