from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):

    def test_bad_maths():
        self.assertEqual(1+1,3)
