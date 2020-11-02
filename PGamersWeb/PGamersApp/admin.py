# //----- IMPORTS -----// 

from django.contrib import admin
from .models import *
from .forms import *

# //----- REGISTROS EN ADMIN  -----// 

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Pedido)