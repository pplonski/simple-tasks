from django.conf.urls import url, include

from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = [
    url(r'^api/<slug>/', include(router.urls)),
]

for u in router.urls:
    print(u)


for u in urlpatterns:
    print(')', u)
