from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path("", views.index, name="home"),
    # ex: /portfolio/
    path("portfolio/", views.portfolio, name="portfolio"),
    # ex: /portfolio/1
    path("portfolio/<int:project_id>", views.portfolio, name="portfolio_detail"),
    # ex: /about/
    path("about/", views.about, name="about_us"),
    # ex: /services/
    path("services/", views.services, name="services"),
    # ex: /services/1
    path("service/<int:service_id>", views.service_detail, name="service_detail"),
    # ex: /contact/
    path("contact/", views.contact, name="contact_us"),
]