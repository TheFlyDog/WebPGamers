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