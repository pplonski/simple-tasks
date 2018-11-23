# DATABASE_URL=0.0.0.0 DATABASE_PORT=5433 pytest apps/accounts/tests_ws.py --verbose --ds server.settings
#
#

import os

from django.test import TestCase
from django.test import Client
import json
import copy
from rest_framework.reverse import reverse
from django.core import mail

from channels.testing import WebsocketCommunicator
from server.routing import application
import pytest
import asyncio
from concurrent.futures import ThreadPoolExecutor

class SignupTestCase(TestCase):

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

    def test_get_organizations(self):
        # create user #1
        self.post_request_and_check(reverse('user_create'), self.params, 201)

    def setUp(self):
        self.params = {'username': 'piotrek',
                    'email': 'piotrek@piotrek.pl',
                    'password': 'verysecret',
                    'organization': 'big co'}

    @pytest.mark.asyncio
    #@pytest.mark.django_db(transaction=True)
    async def test_auth(self):
        print('a')
        communicator = WebsocketCommunicator(application, '/websockets/tasks/')
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_to(text_data="hello")
        response = await communicator.receive_from()
        await communicator.disconnect()
        self.assertTrue(False) # should fail, but it doesnt !
