from django.conf.urls import url, include

from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from accounts.views import MyOrganizationViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'(?P<organization_slug>.+)/tasks', TaskViewSet, base_name='tasks')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]

for u in router.urls:
    print(u, u.pattern, u.pattern.name, u.pattern._regex)

for u in include(router.urls):
    print(u)

'''
\domain\ <- Domains list
\domain\{pk}\ <- One domain, from {pk}
\domain\{domain_pk}\nameservers\ <- Nameservers of domain from {domain_pk}
\domain\{domain_pk}\nameservers\{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}


router = routers.SimpleRouter()
router.register(r'organization', MyOrganizationViewSet)

domains_router = routers.NestedSimpleRouter(router, r'organization', lookup='organization')
domains_router.register(r'tasks', TaskViewSet, base_name='organization-tasks')
# 'base_name' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/


urlpatterns = [
    url(r'^', include(domains_router.urls)),
]


'''
