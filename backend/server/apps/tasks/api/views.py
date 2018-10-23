from rest_framework import viewsets
from tasks.models import Task
from .serializers import TaskSerializer

from django.db import transaction

from worker.simple_worker import WORKERS
from worker.simple_worker import task_add

from rest_framework.exceptions import APIException
import time
import copy

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(state = "CREATED")
                job_params = copy.deepcopy(serializer.validated_data['params']) # dont want to see db_id in returned params
                job_params['db_id'] = instance.id
                transaction.on_commit(lambda: task_add.delay(job_params))
        except Exception as e:
            raise APIException(str(e))

    def perform_destroy(self, instance):
        try:
            with transaction.atomic():
                instance.delete()
                transaction.on_commit(lambda: WORKERS.control.revoke(instance.task_id, terminate=True))
        except Exception as e:
            raise APIException(str(e))
