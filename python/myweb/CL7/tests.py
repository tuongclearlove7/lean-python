from os import CLD_CONTINUED
from urllib import response
from django.test import TestCase, SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_CL7_page_status(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

# Create your tests here.
    













