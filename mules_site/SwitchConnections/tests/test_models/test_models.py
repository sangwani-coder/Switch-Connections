from django.test import TestCase
from SwitchConnections.models import (
    ServiceCategory, ServiceListings,
    ProjectCategory, ProjectListings,
    TeamMembers, CompanyInformation,
    ContactInformation, ContactFormSubmissions,
    BannerImage,
    )

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from SwitchConnections.models import delete_old_image

from mules_site.settings import BASE_DIR

# test models
class ServiceCategoryTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ServiceCategory.objects.create(
            category_name="Wood works", category_description="Wood work products")

    def test_category_name_label(self):
        category = ServiceCategory.objects.get(id=1)
        field_label = category._meta.get_field('category_name').verbose_name
        self.assertEqual(field_label, 'category name')

    def test_category_description_label(self):
        category = ServiceCategory.objects.get(id=1)
        field_label = category._meta.get_field('category_description').verbose_name
        self.assertEqual(field_label, 'category description')

    def test_category_name_max_length(self):
        category = ServiceCategory.objects.get(id=1)
        max_length = category._meta.get_field('category_name').max_length
        self.assertEqual(max_length, 100)

    def test_category_description_max_length(self):
        category = ServiceCategory.objects.get(id=1)
        max_length = category._meta.get_field('category_description').max_length
        self.assertEqual(max_length, 250)

    # test custom methods
    def test_object_name_is_category_name(self):
        category = ServiceCategory.objects.get(id=1)
        expected_object_name = f'{category.category_name}'
        self.assertEqual(str(category), expected_object_name)

class ServiceListingsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = ServiceCategory.objects.create(
            category_name="Wood works", category_description="Wood work products")
        ServiceListings.objects.create(
            service_name="desk making", service_description="school furnture",
            service_price='123', service_category=category,
            )
        
    def test_service_name_label(self):
        service = ServiceListings.objects.get(id=1)
        field_label = service._meta.get_field('service_name').verbose_name
        self.assertEqual(field_label, 'service name')

    def test_service_description_label(self):
        service = ServiceListings.objects.get(id=1)
        field_label = service._meta.get_field('service_description').verbose_name
        self.assertEqual(field_label, 'service description')

    def test_service_price_label(self):
        service = ServiceListings.objects.get(id=1)
        field_label = service._meta.get_field('service_price').verbose_name
        self.assertEqual(field_label, 'service price')

    def test_service_category_label(self):
        service = ServiceListings.objects.get(id=1)
        field_label = service._meta.get_field('service_category').verbose_name
        self.assertEqual(field_label, 'service category')


    def test_service_name_max_length(self):
        service = ServiceListings.objects.get(id=1)
        max_length = service._meta.get_field('service_name').max_length
        self.assertEqual(max_length, 100)

    def test_service_description_max_length(self):
        service = ServiceListings.objects.get(id=1)
        max_length = service._meta.get_field('service_description').max_length
        self.assertEqual(max_length, 250)

    def test_service_price_max_length(self):
        service = ServiceListings.objects.get(id=1)
        max_length = service._meta.get_field('service_price').max_length
        self.assertEqual(max_length, 10)

    # test custom methods
    def test_object_name_is_service_name(self):
        service = ServiceListings.objects.get(id=1)
        expected_object_name = f'{service.service_name}'
        self.assertEqual(str(service), expected_object_name)

    def test_get_absolute_url(self):
        service = ServiceListings.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(service.get_absolute_url(), '/service/1')

class ProjectCategoryTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ProjectCategory.objects.create(
            category_name="Test category", category_description="test category description")

    def test_category_name_label(self):
        category = ProjectCategory.objects.get(id=1)
        field_label = category._meta.get_field('category_name').verbose_name
        self.assertEqual(field_label, 'category name')

    def test_category_description_label(self):
        category = ProjectCategory.objects.get(id=1)
        field_label = category._meta.get_field('category_description').verbose_name
        self.assertEqual(field_label, 'category description')

    def test_category_name_max_length(self):
        category = ProjectCategory.objects.get(id=1)
        max_length = category._meta.get_field('category_name').max_length
        self.assertEqual(max_length, 100)

    def test_category_description_max_length(self):
        category = ProjectCategory.objects.get(id=1)
        max_length = category._meta.get_field('category_description').max_length
        self.assertEqual(max_length, 1000)

    # test custom methods
    def test_object_name_is_category_name(self):
        category = ProjectCategory.objects.get(id=1)
        expected_object_name = f'{category.category_name}'
        self.assertEqual(str(category), expected_object_name)

class ProjectsListingsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = ProjectCategory.objects.create(
            category_name="Test category name", category_description="Test category description")
        image = str(BASE_DIR) + 'static/img/brass.jpg'
        ProjectListings.objects.create(
            project_name="test project", project_description="test project desc",
            project_images=image, project_category=category,
            )
        
    def test_project_name_label(self):
        project = ProjectListings.objects.get(id=1)
        field_label = project._meta.get_field('project_name').verbose_name
        self.assertEqual(field_label, 'project name')

    def test_project_description_label(self):
        project = ProjectListings.objects.get(id=1)
        field_label = project._meta.get_field('project_description').verbose_name
        self.assertEqual(field_label, 'project description')

    def test_project_images_label(self):
        project = ProjectListings.objects.get(id=1)
        field_label = project._meta.get_field('project_images').verbose_name
        self.assertEqual(field_label, 'project images')

    def test_project_category_label(self):
        project = ProjectListings.objects.get(id=1)
        field_label = project._meta.get_field('project_category').verbose_name
        self.assertEqual(field_label, 'project category')


    def test_project_name_max_length(self):
        project = ProjectListings.objects.get(id=1)
        max_length = project._meta.get_field('project_name').max_length
        self.assertEqual(max_length, 100)

    def test_project_description_max_length(self):
        project = ProjectListings.objects.get(id=1)
        max_length = project._meta.get_field('project_description').max_length
        self.assertEqual(max_length, 1000)

    # test custom methods
    def test_object_name_is_project_name(self):
        project = ProjectListings.objects.get(id=1)
        expected_object_name = f'{project.project_name}'
        self.assertEqual(str(project), expected_object_name)

    def test_get_absolute_url(self):
        project = ProjectListings.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(project.get_absolute_url(), '/portfolio/1')


class TeamMembersTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        image = str(BASE_DIR) + 'static/img/brass.jpg'
        TeamMembers.objects.create(
            name='test member', position='test position',
            bio='test bio', profile_picture=image)
        
    def test_member_name_label(self):
        member = TeamMembers.objects.get(id=1)
        field_label = member._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_member_position_label(self):
        member = TeamMembers.objects.get(id=1)
        field_label = member._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    def test_member_bio_label(self):
        member = TeamMembers.objects.get(id=1)
        field_label = member._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_member_profile_label(self):
        member = TeamMembers.objects.get(id=1)
        field_label = member._meta.get_field('profile_picture').verbose_name
        self.assertEqual(field_label, 'profile picture')

    def test_member_name_max_length(self):
        member = TeamMembers.objects.get(id=1)
        max_length = member._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_member_position_max_length(self):
        member = TeamMembers.objects.get(id=1)
        max_length = member._meta.get_field('position').max_length
        self.assertEqual(max_length, 100)

    def test_member_bio_max_length(self):
        member = TeamMembers.objects.get(id=1)
        max_length = member._meta.get_field('bio').max_length
        self.assertEqual(max_length, 250)

    def test_object_name_is_name_comma_position(self):
        member = TeamMembers.objects.get(id=1)
        expected_object_name = f'{member.name}, {member.position}'
        self.assertEqual(str(member), expected_object_name)
        

class CompanyInformationTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) ->  None:
        CompanyInformation.objects.create(
            mission="test mission", vision="test vision statement",
            history='fake history data')
        
    def test_mission_label(self):
        mission = CompanyInformation.objects.get(id=1)
        field_label = mission._meta.get_field('mission').verbose_name
        self.assertEqual(field_label, 'mission')

    def test_vision_label(self):
        vision = CompanyInformation.objects.get(id=1)
        field_label = vision._meta.get_field('vision').verbose_name
        self.assertEqual(field_label, 'vision')

    def test_history_label(self):
        history = CompanyInformation.objects.get(id=1)
        field_label = history._meta.get_field('history').verbose_name
        self.assertEqual(field_label, 'history')

    def test_mission_max_length(self):
        mission = CompanyInformation.objects.get(id=1)
        max_length = mission._meta.get_field('mission').max_length
        self.assertEqual(max_length, 50)

    def test_vision_max_length(self):
        vision = CompanyInformation.objects.get(id=1)
        max_length = vision._meta.get_field('vision').max_length
        self.assertEqual(max_length, 100)

    def test_history_max_length(self):
        history = CompanyInformation.objects.get(id=1)
        max_length = history._meta.get_field('history').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_mission_comma_vision_comma_history(self):
        infor = CompanyInformation.objects.get(id=1)
        expected_object_name = f'{infor.mission}, {infor.vision}, {infor.history}'
        self.assertEqual(str(infor), expected_object_name)

class ContactInformationTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ContactInformation.objects.create(
            physical_address='test address', phone_number_1='testnumb',
            phone_number_2='test2numb', email_address="test eamail"
        )

    def test_physical_address_label(self):
        address =  ContactInformation.objects.get(id=1)
        field_label = address._meta.get_field('physical_address').verbose_name
        self.assertEqual(field_label, 'physical address')

    def test_phone_number_1_label(self):
        phone =  ContactInformation.objects.get(id=1)
        field_label = phone._meta.get_field('phone_number_1').verbose_name
        self.assertEqual(field_label, 'phone number 1')

    def test_phone_number_2_label(self):
        phone =  ContactInformation.objects.get(id=1)
        field_label = phone._meta.get_field('phone_number_2').verbose_name
        self.assertEqual(field_label, 'phone number 2')

    def test_email_address_label(self):
        email =  ContactInformation.objects.get(id=1)
        field_label = email._meta.get_field('email_address').verbose_name
        self.assertEqual(field_label, 'email address')
        
    # test max lenth
    def test_physical_address_max_length(self):
        address =  ContactInformation.objects.get(id=1)
        max_length = address._meta.get_field('physical_address').max_length
        self.assertEqual(max_length, 100)

    def test_phone_number_max_length(self):
        phone =  ContactInformation.objects.get(id=1)
        max_length = phone._meta.get_field('phone_number_1').max_length
        self.assertEqual(max_length, 13)

    def test_phone_number_2_max_length(self):
        phone =  ContactInformation.objects.get(id=1)
        max_length = phone._meta.get_field('phone_number_2').max_length
        self.assertEqual(max_length, 13)

    def test_email_address_max_length(self):
        email =  ContactInformation.objects.get(id=1)
        max_length = email._meta.get_field('email_address').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_email_address_comma_phone_number_1(self):
        infor = ContactInformation.objects.get(id=1)
        expected_object_name = f'{infor.email_address}, {infor.phone_number_1}'
        self.assertEqual(str(infor), expected_object_name)
    

class ContactFormSubmissionTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ContactFormSubmissions.objects.create(
            name='test name', email='test email',
            message='test message', mobile='test mobile'
        )

    def test_contact_name_label(self):
        name = ContactFormSubmissions.objects.get(id=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_contact_created_at_lable(self):
        created = ContactFormSubmissions.objects.get(id=1)
        field_label = created._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_contact_email_label(self):
        email = ContactFormSubmissions.objects.get(id=1)
        field_label = email._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_contact_mobile_label(self):
        mobile = ContactFormSubmissions.objects.get(id=1)
        field_label = mobile._meta.get_field('mobile').verbose_name
        self.assertEqual(field_label, 'mobile')

    def test_contact_message_label(self):
        message = ContactFormSubmissions.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')

    # test max length
    def test_contact_name_length(self):
        name = ContactFormSubmissions.objects.get(id=1)
        max_length = name._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_contact_email_length(self):
        email = ContactFormSubmissions.objects.get(id=1)
        field_length = email._meta.get_field('email').max_length
        self.assertEqual(field_length, 100)

    def test_contact_mobile_length(self):
        mobile = ContactFormSubmissions.objects.get(id=1)
        field_length = mobile._meta.get_field('mobile').max_length
        self.assertEqual(field_length, 100)

    def test_contact_message_length(self):
        message = ContactFormSubmissions.objects.get(id=1)
        field_length = message._meta.get_field('message').max_length
        self.assertEqual(field_length, 1000)

    def test_object_name(self):
        message = ContactFormSubmissions.objects.get(id=1)
        expected_object_name = f'{message.created_at}, {message.name}, {message.message}, {message.mobile}'
        self.assertEqual(str(message), expected_object_name)


class BannerImageTestClass(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        logo = str(BASE_DIR) + 'static/img/brass.jpg'
        cover = str(BASE_DIR) + 'static/img/brass.jpg'
        BannerImage.objects.create(logo_image=logo, cover_image=cover)
    
    def test_logo_label(self):
        logo = BannerImage.objects.get(id=1)
        field_label = logo._meta.get_field('logo_image').verbose_name
        self.assertEqual(field_label, 'logo image')

    def test_cover_label(self):
        cover = BannerImage.objects.get(id=1)
        field_label = cover._meta.get_field('cover_image').verbose_name
        self.assertEqual(field_label, 'cover image')


# class DeleteOldImageTest(TestCase):
#     def setUp(self):
#         # Create a test instance of BannerImage
#         self.brand_image = BannerImage.objects.create()

#     def tearDown(self):
#         # Clean up after the test
#         self.brand_image.cover_image.delete()
#         self.brand_image.logo_image.delete()
#         self.brand_image.delete()

#     def test_delete_old_image(self):
#         # Upload a test cover image and logo image
#         cover_image_file = str(BASE_DIR) + 'static/img/brass.jpg'
#         logo_image_file = str(BASE_DIR) + 'static/img/brass.jpg'
#         self.brand_image.cover_image = cover_image_file
#         self.brand_image.logo_image = logo_image_file
#         self.brand_image.save()

#         # Create a new instance with the same primary key (simulating an update)
#         new_instance = BannerImage(pk=self.brand_image.pk)

#         # Call delete_old_image function
#         delete_old_image(new_instance, "brass.jpg")

#         # Ensure that old images are deleted
#         self.assertFalse(self.brand_image.cover_image.storage.exists(self.brand_image.cover_image.name))
#         self.assertFalse(self.brand_image.logo_image.storage.exists(self.brand_image.logo_image.name))

#         # Ensure that the new_instance cover_image and logo_image are set
#         self.assertEqual(new_instance.cover_image.name, "brass.jpg")
#         self.assertEqual(new_instance.logo_image.name, "brass.jpg")  # Since we set both to "new_cover.jpg"

