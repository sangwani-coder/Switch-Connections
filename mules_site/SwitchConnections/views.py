from django.shortcuts import render, get_object_or_404
from . import models

def index(request):
    banner = models.BannerImage.objects.last()
    template_name = 'SwitchConnections/index.html'
    services = models.ServiceListings.objects.all()
    team = models.TeamMembers.objects.all()
    contact_info = models.ContactInformation.objects.first()
    project_images = models.ProjectImage.objects.all()


    context = {
        'banner':banner,
        'services':services,
        'team':team,
        'contact_info':contact_info,
        'project_images':project_images
    }
    return render(request, template_name, context)

def about(request):
    banner = models.BannerImage.objects.last()
    company_info = models.CompanyInformation.objects.first()
    team = models.TeamMembers.objects.all()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'company_info':company_info,
        'banner':banner,
        'services':services,
        'team':team,
        'contact_info':contact_info
    }

    return render(request, 'SwitchConnections/about.html', context)

def contact(request):
    banner = models.BannerImage.objects.last()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'contact_info':contact_info
    }
    return render(request, 'SwitchConnections/contact.html', context)


def services(request):
    services = models.ServiceListings.objects.all()
    banner = models.BannerImage.objects.last()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'services':services,
        'contact_info':contact_info,
        'services':services
    }
    return render(request, 'SwitchConnections/services.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(models.ServiceListings, pk=service_id)
    services = models.ServiceListings.objects.all()
    banner = models.BannerImage.objects.last()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'services':services,
        'contact_info':contact_info,
        'service':service
    }
    return render(request, 'SwitchConnections/service_details.html', context)

def portfolio(request):
    projects = models.ProjectListings.objects.all()
    project_images = models.ProjectImage.objects.all()
    banner = models.BannerImage.objects.last()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'contact_info':contact_info,
        'projects':projects,
        'project_images':project_images
    }
    return render(request, 'SwitchConnections/portfolio.html', context)


def portfolio_detail(request, project_id):
    project = get_object_or_404(models.ProjectListings, pk=project_id)
    banner = models.BannerImage.objects.last()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'contact_info':contact_info,
        'project':project
    }
    return render(request, 'SwitchConnections/project_details.html', context)
