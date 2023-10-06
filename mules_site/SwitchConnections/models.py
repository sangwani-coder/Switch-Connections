from django.db import models
from django.urls import reverse
from .utils import delete_old_image


# ABOUT US
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(max_length=120)
    profile_picture = models.ImageField(upload_to='static/images/team', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Team members"

    def __str__(self):
        return f'{self.name}, {self.position}'    

class AboutStatement(models.Model):
    text = models.TextField(max_length=3000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "About Statement"

        def __str__(self):
            return self.text
    
# CONTANT US
class ContactInformation(models.Model):
    physical_address = models.CharField(max_length=100)
    phone_number_1 = models.CharField(max_length=13)
    phone_number_2 = models.CharField(max_length=13)
    email_address = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        verbose_name_plural = "Contact information"

    def __str__(self):
        return f'{self.email_address}, {self.phone_number_1}'
    
    
class ContactFormSubmissions(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact form submissions" 

    def __str__(self):
        return f'{self.created_at}, {self.first_name}, {self.last_name}, {self.message}, {self.mobile}'


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
    

#SERVICES
class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Service categories"

    def __str__(self):
        return self.category_name


class ServiceListings(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField(max_length=200)
    service_price = models.CharField(max_length=10, null=True, blank=True)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Service listings"

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.service_name
    

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='static/images/projects/', null=True, blank=True)
    project = models.ForeignKey('ProjectListings', on_delete=models.CASCADE)

# PORTFOLIO
class ProjectListings(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=1000)
    project_images = models.ManyToManyField(ProjectImage, blank=True)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Project Listings"

    def get_absolute_url(self):
        return reverse('portfolio_detail', args=[str(self.id)])

    def __str__(self):
        return self.project_name
    
