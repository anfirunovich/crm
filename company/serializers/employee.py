from rest_framework import serializers

from company.models.employee import Employee, Skill, JobTitle, LanguageKnowledgeLevel


class EmployeeSerializer(serializers.ModelSerializer):
    skills =serializers.StringRelatedField(many=True)

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'sex',
            'phone_number',
            'clothing_size',
            'skills',
            'companies',
            'id',
        )


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            'title',
            'description',
            'id',
        )


class JobTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitle
        fields = (
            'company',
            'employee',
            'job_title',
            'id',
        )


class LanguageKnowledgeLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageKnowledgeLevel
        fields = (
            'employee',
            'language',
            'knowledge_level',
            'id',
        )
