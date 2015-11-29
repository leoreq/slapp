from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from sla_app.views import home,pag_inicio
from django.http import HttpRequest

# Create your tests here.

#class SmokeTest(TestCase):
#
#    def test_bad_maths():
#        self.assertEqual(1+1,3)

class InicioPageTest(TestCase):

    def test_root_urlresolve_to_inicio_view(self):
        found=resolve('/')
        self.assertEqual(found.func,pag_inicio)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=pag_inicio(request)
        self.assertIn(b'<title>Pagina Inicio</title>',response.content)
        self.assertTrue(response.content.startswith(b'<html>'))

class HomePageTest(TestCase):

    def test_root_urlresolve_to_homepage_view(self):
        found=resolve('/slapp/')
        self.assertEqual(found.func,home)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=home(request)
        self.assertContains(response,'<title>SLAPP - Service Level Agreement APP</title>',status_code=200 ,html=True)
        #self.assertTrue(response.content.startswith(b'<html lang="en"><head>'))
        

