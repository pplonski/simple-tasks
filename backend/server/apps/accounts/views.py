import requests

from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from django.urls import reverse

from django.conf import settings

class ActivateByGet(views.APIView):

    def get(self, request, uid, token, format = None):

        payload = {'uid': uid, 'token': token}
        url = '{0}://{1}{2}'.format(settings.PROTOCOL, settings.DOMAIN, reverse('user-activate'))
        response = requests.post(url, data = payload)

        if response.status_code == 204:
            return Response({'detail': 'all good sir'})
        else:
            return Response(response.json())
