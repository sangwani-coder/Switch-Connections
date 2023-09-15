from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /
    path("", views.index, name="home"),
    # ex: /portfolio/
    path("portfolio/", views.portfolio, name="portfolio"),
    # ex: /portfolio/1
    path("portfolio/<int:project_id>/", views.portfolio_detail, name="portfolio_detail"),
    # ex: /about/
    path("about/", views.about, name="about_us"),
    # ex: /services/
    path("services/", views.services, name="services"),
    # ex: /services/1
    path("service/<int:service_id>/", views.service_detail, name="service_detail"),
    # ex: /contact/
    path("contact/", views.contact, name="contact_us"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)