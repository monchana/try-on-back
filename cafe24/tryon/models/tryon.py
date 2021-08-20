from uuid import uuid4
from django.db import models
from tryon.models.common import *
from os.path import splitext


def get_file_path(instance, filename):
    return f"adjusted/{uuid4()}{splitext(filename)[-1]}"


class TryOnImage(BaseModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500, help_text="CDN IMG", blank=True)
    image = models.ImageField(blank=False, upload_to=get_file_path)
    default = models.BooleanField(default=False)
