# //----- IMPORTS -----// 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
#//----- IMPORTS REST_FRAMEWORKS -----//
from rest_framework import viewsets
from .serializer import *

# //----- VISTAS -----// 

# //----- INICIO VISTA -----// 

def inicio(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'PGamersApp/inicio.html', data)

# //----- CONTACTO VISTA -----// 

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST) # recibe los datos del form
        if formulario.is_valid(): #si el form es valido se guarda
            formulario.save()
            data["mensaje"] = "contacto guardado"
            messages.success(request, 'Peticion Enviada correctamente')
        else:
            data["form"] = formulario


    return render(request, 'PGamersApp/contacto.html', data)

# //----- AGREGAR PEDIDO VISTA -----// 

@login_required
def agregar_pedido(request):
    data = {
        'form' : PedidoForm()
    }


    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Pedido Registrado')
        else:
            data["form"] = formulario

    return render(request, 'Pedido/agregar.html', data)

# //----- LISTAR PEDIDO VISTA -----// 

@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    #se recogue el numero de paginas desde la url

    page = request.GET.get('page', 1)

    #se usa try por posibles errores y caida del sistema
    try:
        paginator = Paginator(pedidos, 5) # cantidad de paginas que se requieren por pagina
        pedidos = paginator.page(page) # entrega de la pagina
    except:
        raise Http404

    data = {
        'entity' : pedidos,
        'paginator': paginator
    }

    return render(request, 'Pedido/listar.html', data)

# //----- MODIFICAR PEDIDO VISTA -----// 

@login_required
def modificar_pedido(request, id):
    
    #busca el id obtenido en la url
    pedido = get_object_or_404(Pedido, id=id)

    data = {
        'form' : PedidoForm(instance=pedido)
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_pedido")
        else:
            data["form"] = formulario

    return render(request, 'Pedido/modificar.html', data)

# //----- ELIMINAR PEDIDO VISTA -----// 

@login_required
def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='listar_pedido')

# //----- REGISTRO VISTA -----// 

def registro(request):
    data ={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Te has registrado correctamente!')
            #redirigir al inicio
            return redirect(to="inicio")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)

# //----- PRODUCTOS VISTA -----// 

@login_required
@permission_required('PGamersApp.view_producto')
def productos(request):
    productos = Producto.objects.all()
    #se recogue el numero de paginas desde la url
    page = request.GET.get('page', 1)

    #se usa try por posibles errores y caida del sistema
    try:
        paginator = Paginator(productos, 5) # cantidad de paginas que se requieren por pagina
        productos = paginator.page(page) # entrega de la pagina
    except:
        raise Http404

    data = {
        'entity' : productos,
        'paginator': paginator
    }

    return render(request, 'Producto/productos.html', data)

# //----- AGREGAR PRODUCTOS VISTA -----// 

@login_required
@permission_required('PGamersApp.add_producto')
def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto Agregado')
        else:
            messages.warning(request, 'Datos mal ingresados')
            data["form"] = formulario

    return render(request, 'Producto/agregar.html', data)

# //----- MODIFICAR PRODUCTOS VISTA -----// 

@login_required
@permission_required('PGamersApp.change_producto')
def modificar_producto(request, id):
    
    #busca el id obtenido en la url
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="productos")
        else:
            data["form"] = formulario

    return render(request, 'Producto/modificar.html', data)

# //----- ELIMINAR PRODUCTOS VISTA -----// 

@login_required
@permission_required('PGamersApp.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='productos')

# //----- MARCAS VISTA -----// 

@login_required
@permission_required('PGamersApp.view_marca')
def marcas(request):
    marcas = Marca.objects.all()
    #se recogue el numero de paginas desde la url
    page = request.GET.get('page', 1)

    #se usa try por posibles errores y caida del sistema
    try:
        paginator = Paginator(marcas, 5) # cantidad de paginas que se requieren por pagina
        marcas = paginator.page(page) # entrega de la pagina
    except:
        raise Http404

    data = {
        'entity' : marcas,
        'paginator': paginator
    }

    return render(request, 'Marca/marcas.html', data)

# //----- AGREGAR MARCAS VISTA -----// 

@login_required
@permission_required('PGamersApp.add_marca')
def agregar_marca(request):
    data = {
        'form' : MarcaForm()
    }

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Marca Agregada')
        else:
            data["form"] = formulario


    return render(request, 'Marca/agregar.html', data)

# //----- MODIFICAR MARCAS VISTA -----// 

@login_required
@permission_required('PGamersApp.change_marca')
def modificar_marca(request, id):
    
    #busca el id obtenido en la url
    marca = get_object_or_404(Marca, id=id)

    data = {
        'form' : MarcaForm(instance=marca)
    }

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="marcas")
        else:
            data["form"] = formulario

    return render(request, 'Marca/modificar.html', data)

# //----- ELIMINAR MARCAS VISTA -----// 

@login_required
@permission_required('PGamersApp.delete_marca')
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='marcas')


# //----- VISTAS REST_FRAMEWORK ------//


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all() #Consulta que trae todos los productos
    serializer_class = ProductoSerializers #Pasa la informacion a formato JSON

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all() #Consulta que trae todos los productos
    serializer_class = MarcaSerializers #Pasa la informacion a formato JSON