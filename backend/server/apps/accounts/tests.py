from django.test import TestCase
from django.test import Client
import json

class SignupTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.params = {'username': 'piotrek',
                        #'email': 'piotrek@piotrek.pl',
                        'password': 'verysecret'}

    def test_create(self):

        request = self.client.post('/auth/users/create/', self.params,
                                                content_type="application/json")


        print(request.json())
        self.assertTrue(request.status_code, 201)
