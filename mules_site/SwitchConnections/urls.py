from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path("", views.index, name="home"),
    # ex: /portfolio/
    path("portfolio/", views.portfolio, name="portfolio"),
    # ex: /about/
    path("about/", views.about, name="about_us"),
    # ex: /services/
    path("services/", views.services, name="services"),
    # ex: /contact/
    path("contact/", views.contact, name="contact_us"),
]