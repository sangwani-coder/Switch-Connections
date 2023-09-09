from django.db import models

class ProjectCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=1000)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=1000)
    project_images = models.ImageField()
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)



