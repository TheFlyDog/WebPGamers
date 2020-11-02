from django.test import TestCase
from .models import *

class ProductoTestCase(TestCase):
 def setUp(self):
  marca1 = Marca.objects.create(id=1, nombre="Pillot")
  Producto.objects.create(id=1, nombre="Audifono Pillot", marca=marca1, precio=1200, descripcion="Audifono Negro")

 def test_producto_marca(self):
  producto1 = Producto.objects.get(nombre="Audifono Pillot",)
  self.assertEqual(producto1.marca.nombre,"Pillot")

 def test_producto_precio(self):
  producto2 = Producto.objects.get(nombre="Audifono Pillot")
  self.assertEqual(producto2.precio*10,12000)

class PedidoTestCase(TestCase):
 def setUp(self):
  marca1 = Marca.objects.create(id=1, nombre="Pillot")
  producto1 = Producto.objects.create(id=2, nombre="Audifono Rocket", marca=marca1, precio=1400, descripcion="Audifono Negro")
  Pedido.objects.create(rut="20464556-6", nombres="Lucio Santy", a_paterno="pipp", a_materno="solly", correo="siss@gmail.com", producto=producto1, cantidad=10)

 def test_pedido_producto(self):
  pedido1 = Pedido.objects.get(rut="20464556-6")
  self.assertEqual(pedido1.producto.nombre, "Audifono Rocket")

 def test_pedido_cantidad(self):
  pedido2 = Pedido.objects.get(rut="20464556-6")
  self.assertEqual(pedido2.cantidad-2, 8)



