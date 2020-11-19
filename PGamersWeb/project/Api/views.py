#//----- IMPORTS REST_FRAMEWORKS -----//

from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from PGamersApp.models import *
from rest_framework import viewsets, permissions
from .serializers import *

# //----- VISTAS REST_FRAMEWORK ------//


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all() #Consulta que trae todos los productos
    serializer_class = PedidoSerializers #Pasa la informacion a formato JSON
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]