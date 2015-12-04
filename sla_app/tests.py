from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from sla_app.views import home,pag_inicio,profile_update
from django.http import HttpRequest
from django.template.loader import render_to_string
from sla_app.models import Company
from django.contrib.auth.models import User

# Create your tests here.

#class SmokeTest(TestCase):
#
#    def test_bad_maths():
#        self.assertEqual(1+1,3)

class HomePageTest(TestCase):

    def test_root_urlresolve_to_homepage_view(self):
        found=resolve('/slapp/')

        self.assertEqual(found.func,home)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=home(request)

        expected_html=render_to_string('sla_app/home.html')

        self.assertEqual(response.content.decode(),expected_html)

class CompanyProfileUpdateTest(TestCase):

    def test_page_urlresolve_to_profile_update_view(self):
        found=resolve('/slapp/profile_update/')

        self.assertEqual(found.func,profile_update)

class CompanyModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_user=User.objects.create_user('testuser1','test@gmail.com',password='testpass')
        first_user.save()

        first_company = Company()
        first_company.user=first_user
        first_company.name = 'New Testing Corp'
        first_company.service='This is a company that tests things'
        first_company.save()

        second_user=User.objects.create_user('testuser2','test2@gmail.com',password='testpass2')
        second_user.save()

        second_company = Company()
        second_company.user=second_user
        second_company.name = 'Old Testing Corp'
        second_company.service='This is a company that should tests things'
        second_company.save()

        saved_items = Company.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[1]
        second_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'New Testing Corp')
        self.assertEqual(second_saved_item.service, 'This is a company that should tests things')



    # for later --> def test_profile_update_can_save_a_POST_request(self):
    # for later -->     request=HttpRequest()
    # for later -->     request.method='POST'
    # for later -->     request.POST['name']='Test Company Name'
    # for later --> 
    # for later -->     response=profile_update(request)
    # for later --> 
    # for later -->     self.assertIn('Test Company Name',response.content.decode())

