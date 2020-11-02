# //----- IMPORTS -----// 

from django.db import models

# //----- CLASES -----// 

# //----- CLASE MARCA -----// 

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# //----- CLASE PRODUCTO -----// 

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

# //----- CLASE CONTACTO -----// 

class Contacto(models.Model):
    opciones_consultas = [
        [0, "consulta"],
        [1, "reclamo"],
        [2, "sugerencia"],
        [3, "felicitaciones"]
    ]
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

# //----- CLASE PEDIDO -----// 

class Pedido(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=50)
    a_materno = models.CharField(max_length=50)
    correo = models.EmailField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto

