from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SwitchConnections.models import (
    BannerImage, AboutStatement,
    TeamMembers, ContactInformation,
    ServiceListings, ProjectListings,
    ServiceCategory)


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create test data
        s_category = ServiceCategory.objects.create(
            category_name='test category')
        self.user = User.objects.create(username="testuser")
        self.brand_image = BannerImage.objects.create(
            cover_image="cover.jpg")
        self.about = AboutStatement.objects.create(text="Test about statement")
        self.team_member = TeamMembers.objects.create(
            name="John Doe", position="Designer", bio="Test bio", profile_picture="pro.jpg")
        self.contact_info = ContactInformation.objects.create(
            physical_address="Test Address", phone_number_1="123-456-7890")
        self.service = ServiceListings.objects.create(
            service_name="Test Service",
            service_description="Test description", service_category=s_category)
        self.project = ProjectListings.objects.create(
            project_name="Test Project",
            project_description="Test description", service_category=s_category)

    def tearDown(self):
        # Clean up after the tests if needed
        pass

    def test_index_view(self):
        # Test the index view
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/index.html")

    def test_about_view(self):
        # Test the about view
        response = self.client.get(reverse("about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/about.html")

    def test_contact_view(self):
        # Test the contact view
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/contact.html")

    def test_portfolio_view(self):
        # Test the portfolio view
        response = self.client.get(reverse("portfolio"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "SwitchConnections/portfolio.html")
