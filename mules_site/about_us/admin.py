from django.contrib import admin
from .models import CompanyInformation, TeamMembers

admin.site.register(CompanyInformation)
admin.site.register(TeamMembers)