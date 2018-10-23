from django.contrib import admin

# Register your models here.
from .models import Task

class TaskModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Task

admin.site.register(Task, TaskModelAdmin)
