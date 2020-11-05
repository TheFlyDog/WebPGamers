# //----- IMPORTS -----// 

from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

# //----- FORMULARIOS -----// 

# //----- FORMULARIO CONTACTO -----// 

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

# //----- FORMULARIO PEDIDO -----// 

class PedidoForm(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = ['rut','nombres', 'apellido', 'correo', 'producto','cantidad']

        widgets = {
            'rut': forms.TextInput(
                attrs={'oninput':'checkRut(rut)',
                'placeholder': 'EJ: 204313432 (sin puntos ni guiones'}
            ),

            'correo': forms.EmailInput(
                attrs={'placeholder': 'micorreo@gmail.com',
                'pattern': '[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}'}
            ),
        }

# //----- FORMULARIO CREACION DE USUARIO -----// 
    
class CustomUserCreationForm(UserCreationForm):

    # //----- COMPROBAR SI EXISTE EL USUARIO -----// 
    def clean_username(self):
        username = self.cleaned_data["username"]
        existe = User.objects.filter(username__iexact=username).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        return username
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

        widgets = {
            'correo': forms.EmailInput(
                attrs={'placeholder': 'micorreo@gmail.com',
                'pattern': '[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}'}
            ),
        }

# //----- FORMULARIO MARCA -----// 

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

# //----- FORMULARIO PRODUCTO -----// 

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'