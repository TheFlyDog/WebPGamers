from django.urls import path, include
from .views import *
from rest_framework import routers #Ruta API

router = routers.DefaultRouter() #Rutas de la api por defecto
router.register('pedidos', PedidoViewSet) #Registra la vista de los productos
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)), #Incluye las urls de la api
]