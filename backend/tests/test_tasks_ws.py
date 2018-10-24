
import unittest
import requests
import time
import json
from websocket import create_connection
from websocket._exceptions import WebSocketTimeoutException
from test_tasks_base import TestTasksBase

class TestTasksWebSocket(TestTasksBase):

    def test_ws_progress(self):

        ws = create_connection(self.get_server_ws())

        task = self.create_task(2,2)
        self.assertEqual(task['state'], 'CREATED')
        result =  json.loads(ws.recv())
        ws.close()

        self.assertTrue('data' in result)
        self.assertTrue('progress' in result['data'])
        self.assertTrue('db_id' in result['data'])
        self.assertEqual(task['id'], result['data']['db_id'])

    def test_ws_ends_success(self):

        ws = create_connection(self.get_server_ws())

        task = self.create_task(2,0)
        self.assertEqual(task['state'], 'CREATED')

        ws.settimeout(0.3) # timeout in seconds
        for i in range(10):
            try:
                result =  json.loads(ws.recv())
            except WebSocketTimeoutException as e:
                result = None

            if result is None:
                continue

            if 'SUCCESS' == result['data']['state']:
                break
        ws.close()
        # the last result shoudl be SUCCESS
        self.assertEqual('SUCCESS', result['data']['state'])


    def test_ws_fail_with_exception(self):

        ws = create_connection(self.get_server_ws())

        task = self.create_task(2,-2)
        self.assertEqual(task['state'], 'CREATED')

        result =  json.loads(ws.recv())

        if 'PROGRESS' == result['data']['state']:
            result =  json.loads(ws.recv())

        ws.close()

        self.assertTrue('data' in result)
        self.assertTrue('state' in result['data'])
        self.assertTrue('db_id' in result['data'])
        self.assertEqual('FAILURE', result['data']['state'])

    def test_ws_fail_with_segfault(self):

        ws = create_connection(self.get_server_ws())

        task = self.create_task(-2,2)
        self.assertEqual(task['state'], 'CREATED')
        result =  json.loads(ws.recv())


        if 'PROGRESS' == result['data']['state']:
            result =  json.loads(ws.recv())


        ws.close()

        self.assertTrue('data' in result)
        self.assertTrue('state' in result['data'])
        self.assertTrue('db_id' in result['data'])
        self.assertEqual('FAILURE', result['data']['state'])
