''' This class updates the task in DB '''
import os
import sys
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER_DIR = os.path.join(BACKEND_DIR, 'server')
sys.path.insert(0, SERVER_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
import django
django.setup()

from tasks.models import Task
from django.core.exceptions import ObjectDoesNotExist

from server.asgi import *
from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync


from django.db import transaction

class TaskUpdater:

    @staticmethod
    def update_db(db_id = None, task_id = None, new_state = None, new_result = None):
        if db_id is None and task_id is None:
            raise Exception('You need to specify db_id or task_id to access task.')
        with transaction.atomic():
            try:
                if db_id is not None:
                    task = Task.objects.select_for_update().get(pk=db_id)
                elif task_id is not None:
                    task = Task.objects.select_for_update().get(task_id=task_id)
                if task_id is not None: task.task_id = task_id
                if new_state is not None: task.state = new_state
                if new_result is not None: task.result = new_result
                task.save()
                return task.id
            except ObjectDoesNotExist as e:
                print('Task does not exist in DB!')
            except Exception as e:
                print('Exception in TaskUpdater', str(e))
        return None

    @staticmethod
    def update_ws(msg):
        # send to channel
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("tasks", msg)
