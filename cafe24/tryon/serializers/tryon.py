from rest_framework import serializers
from tryon.models.models import TryOnImage


class TryOnImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnImage
        fields = '__all__'
