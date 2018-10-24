
import unittest
import requests
import time
import json
from websocket import create_connection
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
        pass
        '''
        ws = create_connection(self.get_server_ws())

        task = self.create_task(2,0)
        self.assertEqual(task['state'], 'CREATED')

        ws.settimeout(0.1)
        for i in range(10):
            result =  json.loads(ws.recv())
            print(i, result)
            if 'PROGRESS' == result['data']['state']:
                continue
            else:
                break

        ws.close()
        
        '''


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
