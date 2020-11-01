from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    precio = models.IntegerField()
    descripcion = models.TextField()
    fec_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre


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

class Pedido(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=50)
    a_materno = models.CharField(max_length=50)
    correo = models.EmailField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    def __str__(self):
        return self.id

