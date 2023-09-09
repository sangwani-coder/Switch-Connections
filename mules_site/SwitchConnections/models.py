from django.db import models


# ABOUT US
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)
    profile_picture = models.ImageField()

    class Meta:
        verbose_name_plural = "Team members"

    def __str__(self):
        return self.name
    
class CompanyInformation(models.Model):
    mission = models.CharField(max_length=500)
    vision = models.CharField(max_length=500)
    history = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Company information"

    def __str__(self):
        return self.vision
    

# CONTANT US
class ContactInformation(models.Model):
    physical_address = models.CharField(max_length=100)
    phone_number_1 = models.CharField(max_length=13)
    phone_number_2 = models.CharField(max_length=13)
    email_address = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Contact information"

    def __str__(self):
        return self.physical_address
    
    
class ContactFormSubmissions(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact form submissions" 

    def __str__(self):
        return self.name


# HOME
class CoverImage(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField()
    description = models.CharField(max_length=150)


# PORTFOLIO
class ProjectCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Project Categories"

    def __str__(self) -> str:
        return self.category_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=1000)
    project_images = models.ImageField()
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)

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
    service_description = models.CharField(max_length=100)
    service_price = models.CharField(max_length=10)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Service listings"

    def __str__(self):
        return self.service_name
    
