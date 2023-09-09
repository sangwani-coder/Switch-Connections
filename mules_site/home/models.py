from django.db import models

class CoverImage(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField()
    description = models.CharField(max_length=150)