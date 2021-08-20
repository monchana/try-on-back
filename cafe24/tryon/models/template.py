from django.db import models
from tryon.models.common import *


class TemplatePage(PartModel, BaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    single_line = models.TextField()
    grid = models.TextField()
    zigzag = models.TextField()
