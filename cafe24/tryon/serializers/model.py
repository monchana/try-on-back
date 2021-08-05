from rest_framework import serializers
from tryon.models import Models


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ('id', 'image',)
