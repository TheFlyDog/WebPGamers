from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'PGamersApp/inicio.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST) # recibe los datos del form
        if formulario.is_valid(): #si el form es valido se guarda
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario


    return render(request, 'PGamersApp/contacto.html', data)

def agregar_pedido(request):
    data = {
        'form' : PedidoForm
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto Registrado')
        else:
            data["form"] = formulario


    return render(request, 'Pedido/agregar.html', data)

def listar_pedidos(request):
    pedidos = Pedido.objects.all()

    data = {
        'pedidos' : pedidos
    }

    return render(request, 'Pedido/listar.html', data)

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

def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='listar_pedido')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserRegisterForm()
        
    context = { 'form': form }
    return redirect(to='inicio')