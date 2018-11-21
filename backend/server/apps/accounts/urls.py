from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import ActivateUserByGet
from .views import MyUserCreateView
from .views import MyUserOrganizationList

from django.contrib.auth import get_user_model
from djoser import views
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register('users', views.UserViewSet)
User = get_user_model()

urlpatterns = [
    url(r'^users/create/?$', MyUserCreateView.as_view(), name='user_create'),
    #url(r'^users/me/?$', views.UserView.as_view(), name='user'),
    #url(r'^users/create/?$', views.UserCreateView.as_view(), name='user-create'),
    url(
        r'^users/delete/?$',
        views.UserDeleteView.as_view(),
        name='user_delete'
    ),
    url(
        r'^users/activate/?$',
        views.ActivationView.as_view(),
        name='user_activate'
    ),
    url(r'^password/?$', views.SetPasswordView.as_view(), name='set_password'),
    url(
        r'^password/reset/?$',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        r'^password/reset/confirm/?$',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    #url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    path('activate/<str:uid>/<str:token>/', ActivateUserByGet.as_view()),

    url(
        r'^user/organization/?$',
        MyUserOrganizationList.as_view(),
        name='user_organization'
    ),
]
