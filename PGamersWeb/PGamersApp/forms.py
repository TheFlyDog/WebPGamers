from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = ['rut','nombres', 'a_paterno', 'a_materno', 'correo', 'producto']
    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']