from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^tasks/$', consumers.TasksConsumer),
]
