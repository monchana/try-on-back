
from rest_framework import serializers

from tryon.models import Product, ProductNB


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'part')


class ProductNBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNB
        fields = ('id', 'title', 'image', 'part', 'product')
