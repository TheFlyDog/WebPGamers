from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "precio"]
    list_per_page = 10

admin.site.register(Marca)
admin.site.register(Producto ,ProductAdmin)
admin.site.register(Contacto)
admin.site.register(Pedido)