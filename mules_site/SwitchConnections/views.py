from django.shortcuts import render


def index(request):
    return render(request, 'SwitchConnections/index.html')

def about(request):
    return render(request, 'SwitchConnections/about.html')

def contact(request):
    return render(request, 'SwitchConnections/contact.html')


def services(request):
    return render(request, 'SwitchConnections/services.html')


def portfolio(request):
    return render(request, 'SwitchConnections/portfolio.html')

