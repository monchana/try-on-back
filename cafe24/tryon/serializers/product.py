
from rest_framework import serializers

from tryon.models import Product, ProductNB


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductNBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNB
        fields = '__all__'
