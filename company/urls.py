from rest_framework.routers import DefaultRouter

from company.views.company import CompanyViewSet
from company.views.employee import EmployeeViewSet, SkillViewSet, JobTitleViewSet
from company.views.language import LanguageViewSet
from company.views.location import LocationViewSet


router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='company')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('locations', LocationViewSet, basename='location')
router.register('skills', SkillViewSet, basename='skill')
router.register('job_titles', JobTitleViewSet, basename='job_title')
router.register('languages', LanguageViewSet, basename='language')


urlpatterns = router.urls
