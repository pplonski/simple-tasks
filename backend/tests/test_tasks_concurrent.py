import unittest
import requests
import time
from test_tasks_base import TestTasksBase

#from multiprocessing.dummy import Pool as ThreadPool

import threading

class TestTasksConcurrent(TestTasksBase):

    def single_task_create(self):
        task = self.create_task(0, 1)
        self.assertEqual(task['state'], 'CREATED')
        #print(task)
        self.task_ids += [task['id']]

    def multi_task_create(self):
        for i in range(10):
            self.single_task_create()


    def test_concurrent_create(self):
        self.task_ids = []
        threads = []
        for t in range(10):
            t = threading.Thread(target=self.multi_task_create)
            t.start()
            threads += [t]

        for t in threads: t.join()

        time.sleep(1)

        for i, single_task_id in enumerate(self.task_ids):
            task = self.get_task(single_task_id)
            #print(i, '->', single_task_id, task['state'], task['result'], task['task_id'], task['task_id'] != '')
            self.assertTrue(task['task_id'] is not None and task['task_id'] != '')
            self.assertEqual(task['id'], single_task_id)
            self.assertEqual(task['state'], 'SUCCESS')
            self.assertEqual(task['result']['data'], 1)
