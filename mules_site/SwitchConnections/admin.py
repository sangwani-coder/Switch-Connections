from django.contrib import admin
from .models import ServiceCategory, ServiceListings
from .models import TeamMembers, AboutStatement
from .models import ProjectListings, ProjectImage
from .models import BannerImage, LogoImage
from .models import ContactFormSubmissions, ContactInformation


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'service_category']


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ["image", "project"]


class AboutStatementAdmin(admin.ModelAdmin):
    list_display = ["text"]


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'bio', 'profile_picture']


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'mobile', 'message', 'created_at']


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['physical_address', 'phone_number_1', 'phone_number_1',
                    'email_address', "facebook", "twitter", "instagram"]


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


class ServiceListingAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_description',
                    'service_price', 'service_category']


class BannerAdmin(admin.ModelAdmin):
    list_display = ["cover_image"]


class LogoAdmin(admin.ModelAdmin):
    list_display = ["logo_image"]


# ABOUT_US
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(AboutStatement, AboutStatementAdmin)
# CONTACT US
admin.site.register(ContactFormSubmissions, ContactFormAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
# Banner
admin.site.register(BannerImage, BannerAdmin)
# Logo
admin.site.register(LogoImage, LogoAdmin)
# PORTFOLIO
admin.site.register(ProjectListings, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
# SERVICES
admin.site.register(ServiceListings, ServiceListingAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)

admin.site.site_title = "site admin"
admin.site.site_header = "Switch Connections administration"
# username: admin pass: test#123
