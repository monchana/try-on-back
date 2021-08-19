from rest_framework import serializers
from tryon.models import TemplatePage


class TemplateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePage
        fields = '__all__'


class TemplatePostSerializer(serializers.Serializer):
    tryon_ids = serializers.ListField(child=serializers.IntegerField())
