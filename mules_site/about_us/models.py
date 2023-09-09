from django.db import models

class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)
    profile_picture = models.ImageField()
    
class CompanyInformation(models.Model):
    mission = models.CharField(max_length=500)
    vision = models.CharField(max_length=500)
    history = models.CharField(max_length=500)