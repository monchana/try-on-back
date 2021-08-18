from rest_framework import serializers
from tryon.models import TryOnImage


class TryOnImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnImage
        fields = ('id', 'name', 'template', 'image', 'default')


class RegisterTemplateSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
    productnb_id = serializers.IntegerField()
    layout = serializers.CharField()
    title = serializers.CharField()
