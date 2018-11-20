from django.test import TestCase
from django.test import Client
import json
import copy
from rest_framework.reverse import reverse
from django.core import mail

class SignupTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.params = {'username': 'piotrek',
                    'email': 'piotrek@piotrek.pl',
                    'password': 'verysecret',
                    'organization': 'big co'}

    def post_request_and_check(self, url, params, status_code, token = None):
        headers = {}
        if token:
            headers = {'HTTP_AUTHORIZATION': 'Token '+token}
        request = self.client.post(url, params, content_type="application/json", **headers)
        if request.status_code != status_code:
            print('Print details before fails')
            print(request.status_code)
            print(request.json())
        self.assertEqual(request.status_code, status_code)
        if status_code in [200, 201]:
            return request.json()
        return None

    def test_create_and_delete(self):
        # create user
        self.post_request_and_check(reverse('user_create'), self.params, 201)
        # login
        token = self.post_request_and_check(reverse('login'), self.params, 200).get('auth_token')
        # delete
        self.post_request_and_check(reverse('user_delete'),
                        {'current_password': self.params['password']}, 204, token)

    def test_create_duplicates(self):
        # create user
        self.post_request_and_check(reverse('user_create'), self.params, 201)
        # create the same user
        self.post_request_and_check(reverse('user_create'), self.params, 400)
        # the same user but with new email - should still fail
        self.new_params = copy.deepcopy(self.params)
        self.new_params['email'] = 'piotrek2@piotrek.pl'
        self.post_request_and_check(reverse('user_create'), self.new_params, 400)
        # set new organization
        self.new_params['organization'] = 'big co 2'
        self.post_request_and_check(reverse('user_create'), self.new_params, 201)

    def test_reset_password(self):
        pass

    def atest_delete2(self):

        mail.send_mail(
            'Subject here',
            'Here is the message. 123',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        print(mail.outbox)
        print(len(mail.outbox))
        print(mail.outbox[0].subject)
        print(mail.outbox[0].body)


    def test_missing_values(self):
        params = {'username': 'piotrek',
                    'password': 'verysecret'}

        self.post_request_and_check(reverse('user_create'), params, 400)
        params['organization'] = 'very big co'
        self.post_request_and_check(reverse('user_create'), params, 400)
        params['email'] = 'piotrek@piotrek.pl'
        self.post_request_and_check(reverse('user_create'), params, 201)
