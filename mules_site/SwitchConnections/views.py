from django.shortcuts import render, get_object_or_404
from . import models

def index(request):
    images = models.BrandImages.objects.all()
    return render(request, 'SwitchConnections/index.html', {'images':images})

def about(request):
    company_info = models.CompanyInformation.objects.first()
    team = models.TeamMembers.objects.all()
    return render(request, 'SwitchConnections/about.html', {'team':team, 'company_info':company_info})

def contact(request):
    contact_info = models.ContactInformation.objects.first()
    return render(request, 'SwitchConnections/contact.html', {'contact_info':contact_info})


def services(request):
    services = models.ServiceListings.objects.all()
    return render(request, 'SwitchConnections/services.html', {'services':services})

def service_detail(request, service_id):
    service = get_object_or_404(models.ServiceListings, pk=service_id)
    return render(request, 'SwitchConnections/service_details.html', {'service':service})

def portfolio(request):
    projects = models.ProjectListings.objects.all()
    return render(request, 'SwitchConnections/portfolio.html', {'projects':projects})


def portfolio_detail(request, project_id):
    project = get_object_or_404(models.ProjectListings, pk=project_id)
    return render(request, 'SwitchConnections/project_details.html', {'project':project})
