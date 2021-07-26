from django.db import models


class Model(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    image = models.ImageField(blank=False, upload_to='models')

    class Meta:
        ordering= ['id']
        verbose_name = 'Image_models'

    def __int__(self):
        return self.id

    def get_id(self):
        return self.id


class Product(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    image = models.ImageField(blank=False, upload_to='products')
    part = models.CharField(max_length=50)

    def __int__(self):
        return self.id


class ProductNB(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    image = models.ImageField(blank=False, upload_to='background_crop')
    title = models.CharField(max_length=200)
    part = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

# 어차피 3개면 그냥 format 3개 return하게 할까?
class TemplatePage(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    part = models.CharField(max_length=50)
    single_line = models.TextField()
    grid = models.TextField()
    zigzag = models.TextField()


class TryOnImage(models.Model):
    name = models.CharField(max_length=255)
    template = models.ForeignKey(TemplatePage, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='adjusted')
    default = models.BooleanField(default=False)
