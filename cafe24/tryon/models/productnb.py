from uuid import uuid4
from django.db import models
from tryon.models.common import *
from .product import Product
from os.path import splitext


def get_file_path(instance, filename):
    return f"background_crop/{uuid4()}{splitext(filename)[-1]}"


class ProductNB(PartModel, BaseModel):
    url = models.CharField(max_length=500, help_text="CDN IMG", blank=True)
    image = models.ImageField(blank=False, upload_to=get_file_path)
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __int__(self):
        return self.id
