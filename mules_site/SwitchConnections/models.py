from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .utils import delete_old_image


# ABOUT US
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(max_length=1500)
    profile_picture = models.ImageField(upload_to='static/images/team', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Team members"

    def __str__(self):
        return f'{self.name}, {self.position}'
    
class CompanyInformation(models.Model):
    mission = models.CharField(max_length=50)
    vision = models.CharField(max_length=100)
    history = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Company information"

    def __str__(self):
        return f'{self.mission}, {self.vision}, {self.history}'
    

# CONTANT US
class ContactInformation(models.Model):
    physical_address = models.CharField(max_length=100)
    phone_number_1 = models.CharField(max_length=13)
    phone_number_2 = models.CharField(max_length=13)
    email_address = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Contact information"

    def __str__(self):
        return f'{self.email_address}, {self.phone_number_1}'
    
    
class ContactFormSubmissions(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact form submissions" 

    def __str__(self):
        return f'{self.created_at}, {self.name}, {self.message}, {self.mobile}'


# def delete_old_image(instance, filename):
#         print("instance", instance.pk)
#         # If an old image exists, delete it before saving the new one
#         if instance.pk:
#             print('OLD FILE:', instance.pk)
#             old_instance = BannerImage.objects.get(pk=instance.pk)
#             if old_instance.cover_image and old_instance.cover_image != instance.cover_image:
#                 old_instance.cover_image.delete(save=False)
#             if old_instance.logo_image and old_instance.logo_image != instance.logo_image:
#                 old_instance.logo_image.delete(save=False)
#         return "static/images/" + filename

# Cover
class LogoImage(models.Model):
    logo_image = models.ImageField(upload_to="static/logo", null=True)

    class Meta:
        verbose_name_plural = "Logo Image"
    
    def __str__(self):
        return self.logo_image.path

# Cover
class BannerImage(models.Model):
    cover_image = models.ImageField(upload_to=delete_old_image, null=True)
    
    class Meta:
        verbose_name_plural = "Banner Image"

    def __str__(self):
        return self.cover_image.path


# PORTFOLIO
class ProjectCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Project Categories"

    def __str__(self) -> str:
        return self.category_name


class ProjectListings(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=1000)
    project_images = models.ImageField(upload_to='static/images/projects/', null=True, blank=True)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Project Listings"

    def get_absolute_url(self):
        return reverse('portfolio_detail', args=[str(self.id)])

    def __str__(self):
        return self.project_name
    

#SERVICES
class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Service categories"

    def __str__(self):
        return self.category_name


class ServiceListings(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=250)
    service_price = models.CharField(max_length=10)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Service listings"

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.service_name
    
