from django.contrib import admin
from .models import ServiceCategory, ServiceListings
from .models import CompanyInformation, TeamMembers
from .models import Project, ProjectCategory
from .models import CoverImage
from .models import ContactFormSubmissions, ContactInformation


class ServiceListingAdmin(admin.ModelAdmin):
    fields = ['service_name', 'service_description', 'service_price']


#ABOUT_US
admin.site.register(CompanyInformation)
admin.site.register(TeamMembers)
#CONTACT US
admin.site.register(ContactFormSubmissions)
admin.site.register(ContactInformation)
#HOME
admin.site.register(CoverImage)
#PORTFOLIO
admin.site.register(ProjectCategory)
admin.site.register(Project)
#SERVICES
admin.site.register(ServiceListings, ServiceListingAdmin)
admin.site.register(ServiceCategory)
