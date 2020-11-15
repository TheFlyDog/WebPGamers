# //----- IMPORTS -----// 

from django.contrib import admin
from .models import *
from .forms import *

# //----- CLASES -----//


class ProductAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'precio']
    search_fields = ['nombre']
    list_filter = ['marca','precio']
    list_per_page = 5

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['rut','correo','producto','cantidad','total']
    search_fields = ['producto']
    list_filter = ['rut','correo','producto']
    list_per_page = 5

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','tipo_consulta']
    search_fields = ['nombre']
    list_filter = ['correo','tipo_consulta']
    list_per_page = 5
# //----- REGISTROS EN ADMIN  -----// 

admin.site.register(Marca)
admin.site.register(Producto, ProductAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Pedido, PedidoAdmin)