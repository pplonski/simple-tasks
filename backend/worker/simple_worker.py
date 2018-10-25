'''Script with celery tasks'''

import os
import sys
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER_DIR = os.path.join(BACKEND_DIR, 'server')
sys.path.insert(0, SERVER_DIR)

from task_updater import TaskUpdater
from crash_methods import crash_with_segfault, crash_with_import

import time
from celery import Celery
from config import BROKER_URL, REDIS_URL, REDIS_PORT

WORKERS = Celery('simple_worker')
WORKERS.config_from_object('celeryconfig')

class ArgumentNotFoundError(Exception):
    pass


@WORKERS.task(name='worker.worker.task_add', bind=True)
def task_add(self, params):
    ''' Celery task job '''
    TaskUpdater.update_db(db_id=params['db_id'], task_id=self.request.id, new_state='PROGRESS')

    # check the json schema
    for arg in ['arg1', 'arg2', 'db_id']:
        if arg not in params:
            raise ArgumentNotFoundError('Argument {0} is missing'.format(arg))

    # Simulate some crashing ...
    if params['arg1'] < 0: crash_with_segfault()
    if params['arg2'] < 0: crash_with_import()

    for i in range(params['arg1']):
        print(i)
        # celery task update, it will be saved in redis
        self.update_state(state='PROGRESS', meta={'progress': i,
                                                    'db_id': params['db_id']})
        time.sleep(1)

    # Set the state for task
    TaskUpdater.update_db(db_id=params['db_id'], new_state='SUCCESS',
                        new_result={'data': params['arg1']+params['arg2']})
    # Send info to channel
    data = {'state': 'SUCCESS', 'progress': 100, 'db_id': params['db_id']}
    msg = {"type": "task_update_message", "data": data}
    TaskUpdater.update_ws(msg)


    return True
