from django.test import TestCase
from django.test import Client
import json

class TaskTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_params = {"params": {"arg1":2, "arg2":2}}

    def test_create(self):

        request = self.client.get('/api/tasks')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.json()), 0)

        request = self.client.post('/api/tasks', self.task_params,
                                                content_type="application/json")
        self.assertEqual(request.status_code, 201)

        request = self.client.get('/api/tasks')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.json()), 1)

    def test_delete(self):

        request = self.client.post('/api/tasks', self.task_params,
                                                content_type="application/json")
        self.assertEqual(request.status_code, 201)
        my_id = request.json()['id']

        request = self.client.delete('/api/tasks/{0}'.format(my_id))
        self.assertEqual(request.status_code, 204)

        request = self.client.get('/api/tasks')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(request.json()), 0)
