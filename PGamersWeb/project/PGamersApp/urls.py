# //----- IMPORTS -----// 

from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView #importar vistas del login y logout
from rest_framework import routers #Ruta API

router = routers.DefaultRouter() #Rutas de la api por defecto
router.register('productos', ProductoViewSet) #Registra la vista de los productos
router.register('marcas', MarcaViewSet) #Registra la vista de las marcas


# //----- URLS -----// 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('marcas/', marcas, name="marcas"),
    path('agregar-marca/', agregar_marca, name="agregar_marca"),
    path('modificar-marca/<id>/', modificar_marca, name="modificar_marca"),
    path('eliminar-marca/<id>/', eliminar_marca, name="eliminar_marca"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-pedido/', agregar_pedido, name="agregar_pedido"),
    path('listar-pedido/', listar_pedidos, name="listar_pedido"),
    path('modificar-pedido/<id>/', modificar_pedido, name="modificar_pedido"),
    path('eliminar-pedido/<id>/', eliminar_pedido, name="eliminar_pedido"),
    path('registro/', registro, name="registro"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('api/', include(router.urls)), #Incluye las urls de la api
] 