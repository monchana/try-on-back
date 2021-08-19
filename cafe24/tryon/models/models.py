from django.db import models

from tryon.models.common import GenderModel, PartModel


class Models(GenderModel):
    image = models.ImageField(blank=False, upload_to='models')

    class Meta:
        ordering = ['id']
        verbose_name = 'Image_models'

    def __int__(self):
        return self.id

    def get_id(self):
        return self.id


class Product(GenderModel, PartModel):
    image = models.ImageField(blank=False, upload_to='products')

    def __int__(self):
        return self.id


class ProductNB(PartModel):
    url = models.CharField(max_length=500, help_text="CDN IMG", blank=True)
    image = models.ImageField(blank=False, upload_to='background_crop')
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __int__(self):
        return self.id


class TemplatePage(PartModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    single_line = models.TextField()
    grid = models.TextField()
    zigzag = models.TextField()


class TryOnImage(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500, help_text="CDN IMG", blank=True)
    image = models.ImageField(blank=False, upload_to='adjusted')
    default = models.BooleanField(default=False)
