from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from company.models.skill import Skill

from company.serializers.skill import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_active=True).all()