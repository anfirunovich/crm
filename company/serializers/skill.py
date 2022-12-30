from rest_framework import serializers

from company.models.skill import Skill


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            'id',
            'title',
            'description',
        )
