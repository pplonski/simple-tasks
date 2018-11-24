from django.db import models
from django.contrib.postgres.fields import JSONField

from django.utils.timezone import now
from accounts.models import MyUser, MyOrganization

class AutoCreatedField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("editable", False)
        kwargs.setdefault("default", now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)


class Task(models.Model):
    state = models.CharField(max_length=128)
    params = JSONField()
    result = JSONField(default=dict) # default set to empty dict
    task_id = models.CharField(max_length=128)

    created_at = AutoCreatedField()
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    parent_organization = models.ForeignKey(MyOrganization, on_delete=models.CASCADE)
