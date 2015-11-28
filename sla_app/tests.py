from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from sla_app.views import home,pag_inicio

# Create your tests here.

#class SmokeTest(TestCase):
#
#    def test_bad_maths():
#        self.assertEqual(1+1,3)

class HomePageTest(TestCase):

    def test_root_urlresolve_to_homepage_view(self):
        found=resolve('/')
        self.assertEqual(found.func,pag_inicio)
