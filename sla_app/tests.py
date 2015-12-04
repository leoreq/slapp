from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from sla_app.views import home,pag_inicio,profile_update
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

#class SmokeTest(TestCase):
#
#    def test_bad_maths():
#        self.assertEqual(1+1,3)

class InicioPageTest(TestCase):

    def test_root_urlresolve_to_inicio_view(self):
        found=resolve('/pag_inicio/')

        self.assertEqual(found.func,pag_inicio)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=pag_inicio(request)

        expected_html=render_to_string('sla_app/pagina_inicio.html')

        self.assertEqual(response.content.decode(),expected_html)

    def test_pagina_inicio_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = pag_inicio(request)

        self.assertIn('A new list item', response.content.decode())

        expected_html=render_to_string('sla_app/pagina_inicio.html',{
        'new_item_text':'A new list item'
        })

        self.assertEqual(response.content.decode(),expected_html)

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

    # for later --> def test_profile_update_can_save_a_POST_request(self):
    # for later -->     request=HttpRequest()
    # for later -->     request.method='POST'
    # for later -->     request.POST['name']='Test Company Name'
    # for later --> 
    # for later -->     response=profile_update(request)
    # for later --> 
    # for later -->     self.assertIn('Test Company Name',response.content.decode())

