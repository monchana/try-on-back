from os.path import join as pjoin
from django.conf import settings
from rest_framework import serializers
from tryon.models import Models
from tryon.services.try_on_back_modules.tryongenerator.utils.util_module import TryOnUtils


class ModelSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        utils = TryOnUtils()
        utils.pad_overall(img_paths=[instance.image.path], dest_dir=pjoin(
            settings.PRE_DIR, "image"))
        return instance

    class Meta:
        model = Models
        fields = '__all__'
