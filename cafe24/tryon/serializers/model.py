import os
from os.path import join as pjoin
from tryon.services.try_on_back_modules.tryongenerator.vtp_bottom.bottomUtil import BottomUtil
from django.conf import settings
from rest_framework import serializers
from tryon.models import Models
from tryon.services.try_on_back_modules.tryongenerator.utils.util_module import TryOnUtils


class ModelSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        utils = TryOnUtils()
        dest_dir = pjoin(settings.PRE_DIR, "image")
        utils.pad_overall(img_paths=[instance.image.path], dest_dir=dest_dir)
        bottom_util = BottomUtil(root_dir=settings.PRE_DIR)
        b_param = [pjoin(dest_dir, os.path.basename(instance.image.name))]
        bottom_util.save_keypoints(img_paths=b_param)
        bottom_util.image_parse(img_paths=b_param)
        bottom_util.body_masking(img_paths=b_param)
        return instance

    class Meta:
        model = Models
        fields = '__all__'
