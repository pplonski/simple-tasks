from django.db import models
from django.contrib.postgres.fields import JSONField

class Task(models.Model):
    state = models.CharField(max_length=128)
    params = JSONField()
    result = JSONField(default=dict) # default set to empty dict
    task_id = models.CharField(max_length=128)
