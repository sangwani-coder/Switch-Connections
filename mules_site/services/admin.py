from django.contrib import admin
from .models import ServiceCategory, ServiceListings

admin.site.register(ServiceListings)
admin.site.register(ServiceCategory)
