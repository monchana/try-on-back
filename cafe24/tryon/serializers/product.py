
from rest_framework import serializers

from tryon.models import Product, ProductNB


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductNBSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.product.gender

    class Meta:
        model = ProductNB
        fields = '__all__'
