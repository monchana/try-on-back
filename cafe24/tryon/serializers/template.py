from rest_framework import serializers
from tryon.models import TemplatePage


class TemplatePostSerializer(serializers.Serializer):
    model_ids = serializers.ListField(
        child=serializers.IntegerField())
    nobg_id = serializers.IntegerField()


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePage
        fields = ('id', 'name', 'title', 'part',
                  'single_line', 'grid', 'zigzag')
