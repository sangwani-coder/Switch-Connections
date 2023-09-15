from django.contrib import admin
from .models import ServiceCategory, ServiceListings
from .models import CompanyInformation, TeamMembers
from .models import ProjectListings, ProjectCategory
from .models import BannerImage, LogoImage
from .models import ContactFormSubmissions, ContactInformation


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'project_category']

class ProjectCategoryAdmin(admin.ModelAdmin):
     list_display = ['category_name', 'category_description']

class CompanyInforAdmin(admin.ModelAdmin):
    list_display = ['mission', 'vision', 'history']

class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'bio']
    
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'message', 'created_at']
    
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['physical_address', 'phone_number_1', 'phone_number_1', 'email_address']
    
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_description']

class ServiceListingAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_description', 'service_price', 'service_category']


class BannerAdmin(admin.ModelAdmin):
    list_display = ["cover_image"]

class LogoAdmin(admin.ModelAdmin):
    list_display = ["logo_image"]

#ABOUT_US
admin.site.register(CompanyInformation, CompanyInforAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
#CONTACT US
admin.site.register(ContactFormSubmissions, ContactFormAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
#Banner
admin.site.register(BannerImage, BannerAdmin)
# Logo
admin.site.register(LogoImage, LogoAdmin)
#PORTFOLIO
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectListings, ProjectAdmin)
#SERVICES
admin.site.register(ServiceListings, ServiceListingAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)

# username: admin pass: test#123