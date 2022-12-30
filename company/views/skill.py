from rest_framework import viewsets

from company.models.skill import Skill
from company.serializers.skill import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_active=True).all()