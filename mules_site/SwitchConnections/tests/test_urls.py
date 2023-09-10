from django.test import TestCase
from django.urls import reverse
from SwitchConnections import models
from mules_site.settings import BASE_DIR


class ProjectUrlsTestCase(TestCase):
    def test_home_url(self):
        # Test the URL for the home page
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    # Add more test methods for other project-level URLs as needed


class AppUrlsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        p_category = models.ProjectCategory.objects.create(
            category_name="Test category", category_description="test category description")
        image = str(BASE_DIR) + 'static/img/brass.jpg'
        models.ProjectListings.objects.create(
            project_name="test project", project_description="test project desc",
            project_images=image, project_category=p_category,
            )
        s_category = models.ServiceCategory.objects.create(
            category_name="Wood works", category_description="Wood work products")
        models.ServiceListings.objects.create(
            service_name="desk making", service_description="school furnture",
            service_price='123', service_category=s_category,
            )

    def test_home_url(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/index.html")

    def test_portfolio_url(self):
        response = self.client.get(reverse("portfolio"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/portfolio.html")

    def test_portfolio_detail_url(self):
        project_id = 1
        response = self.client.get(reverse("portfolio_detail", args=[project_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/project_details.html")

    def test_about_us_url(self):
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/about.html")

    def test_services_url(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/services.html")

    def test_service_detail_url(self):
        service_id = 1
        response = self.client.get(reverse("service_detail", args=[service_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/service_details.html")

    def test_contact_us_url(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/contact.html")
