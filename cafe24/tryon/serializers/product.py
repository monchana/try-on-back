
from tryon.services.try_on_back_modules.tryongenerator.utils.util_module import TryOnUtils
from django.conf import settings
from rest_framework import serializers
from os.path import join as pjoin

from tryon.models import Product, ProductNB


class ProductSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        utils = TryOnUtils()
        utils.pad_overall(img_paths=[instance.image.path], dest_dir=pjoin(
            settings.PRE_DIR, "cloth"))
        return instance

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
