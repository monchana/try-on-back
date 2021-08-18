from tryon.serializers.tryon import TryOnImageModelSerializer
from rest_framework import serializers
from tryon.models import TemplatePage


class TemplatePostSerializer(serializers.Serializer):
    model_ids = serializers.ListField(
        child=serializers.IntegerField())
    nobg_id = serializers.IntegerField()


class TemplateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePage
        fields = '__all__'


class CreateTemplateSerializer(serializers.Serializer):
    template = TemplateModelSerializer
    tryon_imgs = TryOnImageModelSerializer(many=True)
