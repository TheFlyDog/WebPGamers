# //----- IMPORTS -----// 

from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView #importar vistas del login y logout

# //----- URLS -----// 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-pedido/', agregar_pedido, name="agregar_pedido"),
    path('listar-pedido/', listar_pedidos, name="listar_pedido"),
    path('modificar-pedido/<id>/', modificar_pedido, name="modificar_pedido"),
    path('eliminar-pedido/<id>/', eliminar_pedido, name="eliminar_pedido"),
    path('registro/', registro, name="registro"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
] 