from django.urls import path, include
from .views import *
from rest_framework import routers #Ruta API

router = routers.DefaultRouter() #Rutas de la api por defecto
router.register('productos', ProductoViewSet) #Registra la vista de los productos
router.register('marcas', MarcaViewSet) #Registra la vista de las marcas

urlpatterns = [
    path('api/', include(router.urls)), #Incluye las urls de la api
]