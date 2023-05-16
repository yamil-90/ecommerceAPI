from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class Login(APIView):
    print('Login')
    
    def get(self, request):
        return JsonResponse({'message': 'this is the login page'}, safe=False)

    def post(self, request):
        return JsonResponse({'message': 'this is the login page'}, safe=False)
    
class RestrictedView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse({'message': 'this is the restricted page'}, safe=False)