from django.test import TestCase
from django.test import Client
import json

class SignupTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.params = {'username': 'piotrek',
                        'email': 'piotrek@piotrek.pl',
                        'password1': 'verysecret',
                        'password2': 'verysecret'}

    def test_create(self):

        request = self.client.post('/rest-auth/registration/', self.params,
                                                content_type="application/json")

        print(request)
        print(request.json())
        print(request.status_code)
