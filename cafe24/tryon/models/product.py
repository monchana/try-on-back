from django.db import models
from tryon.models.common import *
from os.path import splitext
from uuid import uuid4


def get_file_path(instance, filename):
    return f"products/{uuid4()}{splitext(filename)[-1]}"


class Product(GenderModel, PartModel, BaseModel):
    image = models.ImageField(blank=False, upload_to=get_file_path)

    def __int__(self):
        return self.id
