from django.shortcuts import render

from rest_framework import views

class ActivateByGet(views.APIView):

    def get(self, request, format = None):
        print('Activate')
        
