#//----- IMPORTS REST_FRAMEWORKS -----//

from django.shortcuts import render,redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from PGamersApp.models import *
from rest_framework import viewsets
from .serializers import *

# //----- VISTAS REST_FRAMEWORK ------//


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all() #Consulta que trae todos los productos
    serializer_class = ProductoSerializers #Pasa la informacion a formato JSON

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all() #Consulta que trae todos los productos
    serializer_class = MarcaSerializers #Pasa la informacion a formato JSON

class Login(APIView):
    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
