from django.test import TestCase
from django.test import Client
import json

from rest_framework.reverse import reverse

class SignupTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create(self):
        params = {'username': 'piotrek',
                    'email': 'piotrek@piotrek.pl',
                    'password': 'verysecret',
                    'organization': 'big co'}

        request = self.client.post('/auth/users/create/', params,
                                                content_type="application/json")

        print(request.status_code, request.json())
        self.assertEqual(request.status_code, 201)

        request = self.client.post(reverse('login'), params,
                                                content_type="application/json")
        print(request.status_code, request.json())

        print('-'*50)

        request = self.client.post('/auth/users/create/', params,
                                                content_type="application/json")

        print(request.status_code, request.json())

        print('-'*50)

        params = {'username': 'piotrek',
                    'email': 'piotrek2@piotrek.pl',
                    'password': 'verysecret',
                    'organization': 'big co'}

        request = self.client.post('/auth/users/create/', params,
                                                content_type="application/json")

        print('LAST', request.status_code, request.json())


    '''
    def test_missing_email(self):
        params = {'username': 'piotrek',
                    'password': 'verysecret'}

        request = self.client.post('/auth/users/create/', params,
                                                content_type="application/json")

        #print(request.status_code, request.json())
        self.assertEqual(request.status_code, 400)
    '''
