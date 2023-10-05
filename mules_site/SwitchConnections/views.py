from django.shortcuts import render, get_object_or_404
from . import models
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactFormSubmissionsForm
from django.contrib import messages


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
    about = models.AboutStatement.objects.first()
    team = models.TeamMembers.objects.all()
    contact_info = models.ContactInformation.objects.first()
    context = {
        'banner':banner,
        'services':services,
        'team':team,
        'contact_info':contact_info,
        'about':about
    }

    return render(request, 'SwitchConnections/about.html', context)


class ContactFormView(FormView):
    form_class = ContactFormSubmissionsForm
    template_name = 'SwitchConnections/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the form data to the database
        form.save()
        messages.success(self.request, 'Your message submission was successful!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = models.ContactInformation.objects.first()

        # Add additional context variables here
        context['contact_info'] = contact_info

        return context


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
