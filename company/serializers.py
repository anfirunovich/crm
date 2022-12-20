from crm.company.models import Company


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    info = serializers.CharField(max_length=255)

   
    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.info = validated_data.get("info", instance.info)
        instance.location = validated_data.get("location", instance.location)
        return instance