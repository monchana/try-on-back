from django.db import models as md
from tryon.models.common import *
from os.path import splitext
from uuid import uuid4


def get_file_path(instance, filename):
    return f"models/{uuid4()}{splitext(filename)[-1]}"


class Models(GenderModel, BaseModel, PartModel):
    image = md.ImageField(blank=False, upload_to=get_file_path)
    shop_id = md.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = 'Image_models'

    def __int__(self):
        return self.id

    def get_id(self):
        return self.id
