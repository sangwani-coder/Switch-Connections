from django.test import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.urls import reverse


from SwitchConnections.models import (
    ProjectCategory, ProjectListings,
    ServiceCategory, ServiceListings)


class SeleniumTest(TestCase):
    # Initialize the WebDriver (choose your browser)
        
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # Define the URL of your Django project
        self.base_url = "http://localhost:8000"  # Update with your project's URL

        s_category = ServiceCategory.objects.create(
            category_name='test category', category_description="test description")
        
        p_category = ProjectCategory.objects.create(
            category_name='test category', category_description="test description")
        
        self.service = ServiceListings.objects.create(
            service_name="Test Service",
            service_description="Test description", service_category=s_category)
        
        self.project = ProjectListings.objects.create(
            project_name="Test Project",
            project_description="Test description", project_category=p_category)

    def test_home_page(self):
        print("================Test Home Page===============")
        # Test the Home page
        self.driver.get(self.base_url)    
        assert "Switch Connections - Home" == self.driver.title
        self.driver.quit()


    def test_about_page(self):
        # Test the About Us page
        print("================Test About Page===============")
        self.driver.get(self.base_url + "/about/")
        assert "Switch Connections - About us" == self.driver.title
        time.sleep(0.5)
        self.driver.quit()

    
    def test_contact_page(self):
        # Test the Contact Us page
        print("================Test Contact Page===============")
        self.driver.get(self.base_url + "/contact/")
        self.assertEqual("Switch Connections - Contact us", self.driver.title)
        time.sleep(0.5)
        self.driver.quit()


    def test_service_page(self):
        # Test the services page
        print("================Test Services Page===============")
        self.driver.get(self.base_url + "/services/")
        self.assertEqual("Switch Connections - Services", self.driver.title)
        time.sleep(0.5)
        time.sleep(1)

        # Test the service details page
        s_id = self.service.pk
        s_url = reverse("service_detail", args=[s_id])
        self.driver.get(self.base_url + s_url)
        self.assertEqual("Switch Connections - Service details", self.driver.title)
        time.sleep(1)
        self.driver.quit()


    def test_portfolio_page(self):
        # Test the portfolio page
        print("================Test Portfolio Page===============")
        self.driver.get(self.base_url + "/portfolio/")
        self.assertEqual("Switch Connections - Portfolio", self.driver.title)
        time.sleep(1)

        # Test the portfolio detail page
        p_id = self.project.pk
        p_url = reverse("portfolio_detail", args=[p_id])
        self.driver.get(self.base_url + p_url)
        self.assertEqual("Switch Connections - Project details", self.driver.title)
        time.sleep(1)

        self.driver.quit()
