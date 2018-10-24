import unittest
import requests
import time
from test_tasks_base import TestTasksBase

class TestTasksApi(TestTasksBase):

    def test_create(self):

        task = self.create_task(3,2)
        self.assertEqual(task['state'], 'CREATED')
        time.sleep(1)
        task2 = self.get_task(task['id'])

        self.assertEqual(task2['state'], 'PROGRESS')
        self.assertEqual(task['id'], task2['id'])

        time.sleep(3)

        task3 = self.get_task(task['id'])

        self.assertEqual(task3['state'], 'SUCCESS')
        self.assertEqual(task3['result']['data'], 5)

    def test_task_segfault(self):

        task = self.create_task(-1,2)
        self.assertEqual(task['state'], 'CREATED')

        for i in range(10):
            task2 = self.get_task(task['id'])
            if task2['state'] == 'FAILURE':
                break
            time.sleep(1)

        self.assertEqual(task2['state'], 'FAILURE')
        self.assertTrue('exception' in task2['result'])


    def test_task_exception(self):

        task = self.create_task(1,-2)
        self.assertEqual(task['state'], 'CREATED')
        time.sleep(1)
        task2 = self.get_task(task['id'])

        self.assertEqual(task2['state'], 'FAILURE')
        self.assertTrue('exception' in task2['result'])
