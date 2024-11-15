from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class AnimalsModel(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="Images/")
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=10000)
    curraction = models.CharField(max_length=2000)
    whatcanyoudo = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.title
