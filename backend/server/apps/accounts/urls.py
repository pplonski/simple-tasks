from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import ActivateUserByGet
from .views import MyUserCreateView

urlpatterns = [
    url(r'^auth/users/create/?$', MyUserCreateView.as_view()),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    path('activate/<str:uid>/<str:token>/', ActivateUserByGet.as_view()),
]
