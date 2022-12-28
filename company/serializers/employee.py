from rest_framework import serializers

from company.models.employee import Employee, Skill, JobTitle, LanguageKnowledgeLevel


class EmployeeSerializer(serializers.ModelSerializer):
    skills =serializers.StringRelatedField(many=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'age',
            'sex',
            'phone_number',
            'clothing_size',
            'skills',
            'companies',
        )


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = (
            'id',
            'title',
            'description',
        )


class JobTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTitle
        fields = (
            'id',
            'company',
            'employee',
            'job_title',
        )


class LanguageKnowledgeLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageKnowledgeLevel
        fields = (
            'id',
            'employee',
            'language',
            'knowledge_level',
        )
