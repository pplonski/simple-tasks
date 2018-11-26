import requests

from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from django.urls import reverse

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls.exceptions import NoReverseMatch
from django.utils.timezone import now
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from djoser import utils, signals
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings


from rest_framework import generics, permissions, status, views, viewsets

from accounts.models import Membership
from accounts.models import MyOrganization

from accounts.serializers import OrganizationSerializer

class MyUserOrganizationList(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = ()
    def get_queryset(self):
        user = self.request.user
        return MyOrganization.objects.filter(myuser=user)


class MyOrganizationViewSet(viewsets.ModelViewSet):
    queryset = MyOrganization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MyUserCreateView(generics.CreateAPIView):
    """
    Use this endpoint to register new user.
    """

    serializer_class = settings.SERIALIZERS.user_create
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {"user": user}
        to = [get_user_email(user)]
        if settings.SEND_ACTIVATION_EMAIL:
            settings.EMAIL.activation(self.request, context).send(to)
        elif settings.SEND_CONFIRMATION_EMAIL:
            settings.EMAIL.confirmation(self.request, context).send(to)


from djoser.conf import django_settings


class ActivateUserByGet(views.APIView):
    def get(self, request, uid, token, format=None):
        payload = {"uid": uid, "token": token}

        url = "{0}://{1}{2}".format(
            django_settings.PROTOCOL, django_settings.DOMAIN, reverse("user_activate")
        )
        response = requests.post(url, data=payload)

        if response.status_code == 204:
            return Response({"detail": "all good sir"})
        else:
            return Response(response.json())
