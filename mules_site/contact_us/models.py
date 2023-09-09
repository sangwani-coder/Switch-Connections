from django.db import models

class ContactInformation(models.Model):
    physical_address = models.CharField(max_length=100)
    phone_number_1 = models.CharField(max_length=13)
    phone_number_2 = models.CharField(max_length=13)
    email_address = models.CharField(max_length=100)
    
    
class ContactFormSubmissions(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True) 