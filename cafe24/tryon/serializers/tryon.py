from rest_framework import serializers
from tryon.models import TryOnImage


class TryOnImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnImage
        fields = '__all__'


class GenTryOnSerializer(serializers.Serializer):
    model_ids = serializers.ListField(
        child=serializers.IntegerField())
    nobg_id = serializers.IntegerField()
