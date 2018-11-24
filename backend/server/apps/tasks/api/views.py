from rest_framework import viewsets
from tasks.models import Task
from tasks.api.serializers import TaskSerializer

from django.db import transaction

from worker.simple_worker import WORKERS
from worker.simple_worker import task_add

from rest_framework.exceptions import APIException
from rest_framework import permissions
import time
import copy

from accounts.models import Membership


class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = "You must be the owner of this object."

    def has_permission(self, request, view):
        print("has_permission")
        return True
        print(request.data)
        print(request.data.get("parent_organization"))
        if request.user is None:
            return False
        if not request.user.is_authenticated:
            return False
        if not request.data.get("parent_organization"):
            return False
        try:
            Membership.objects.get(
                user=request.user,
                organization=request.data.get("parent_organization"),
                status__in=["admin", "member"],
            )
        except Membership.DoesNotExist:
            print("Membership does not exist")
            return False
        return True
        # return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print("has_object_permission", obj.created_by, request.user)
        return True #obj.user == request.user


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAuthenticatedAndOwner)

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                print("task perform_create", self.request.user)
                instance = serializer.save(
                    state="CREATED", created_by=self.request.user
                )
                # job_params = copy.deepcopy(serializer.validated_data['params']) # dont want to see db_id in returned params
                # job_params['db_id'] = instance.id
                # transaction.on_commit(lambda: task_add.delay(job_params))
        except Exception as e:
            raise APIException(str(e))

    def perform_destroy(self, instance):
        try:
            with transaction.atomic():
                instance.delete()
                transaction.on_commit(
                    lambda: WORKERS.control.revoke(instance.task_id, terminate=True)
                )
        except Exception as e:
            raise APIException(str(e))
