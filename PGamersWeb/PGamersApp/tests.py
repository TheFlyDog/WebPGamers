from django.test import TestCase
from .models import *

class PedidoTestCase(TestCase):
 def setUp(self):
  marca1 = Marca.objects.create(id=1, nombre="Pillot")
  producto1 = Producto.objects.create(id=1, nombre="Audifono SSS", marca=marca1, precio=1400, descripcion="Audifono Negro")
  Pedido.objects.create(id=1, rut="20464556-6", nombres="Lucio", apellido="soto", correo="siss@gmail.com", producto=producto1, cantidad=2)

 def test_pedido_rut(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.rut,"20464556-6")
  
 def test_pedido_nombres(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.nombres, "Lucio")

 def test_pedido_apellido(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.apellido, "soto")

 def test_pedido_correo(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.correo,"siss@gmail.com")

 def test_pedido_producto(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.producto.nombre,"Audifono SSS")

 def test_pedido_producto_marca(self):
  pedido1 = Pedido.objects.get(id=1)
  self.assertEqual(pedido1.producto.marca.nombre,"Pillot")

class ContactoCase(TestCase):
 def setUp(self):
    Contacto.objects.create(id=1, nombre="Nicolas", correo="nico@gmail.com", tipo_consulta=1, mensaje="bla", avisos=False)
  
 def test_contacto_nombre(self):
  contacto1 = Contacto.objects.get(id=1)
  self.assertEqual(contacto1.nombre,"Nicolas")

 def test_contacto_correo(self):
  contacto1 = Contacto.objects.get(id=1)
  self.assertEqual(contacto1.correo,"nico@gmail.com")

 def test_contacto_tipo_consulta(self):
  contacto1 = Contacto.objects.get(id=1)
  self.assertEqual(contacto1.tipo_consulta,1)

 def test_contacto_mensaje(self):
  contacto1 = Contacto.objects.get(id=1)
  self.assertEqual(contacto1.mensaje,"bla")

 def test_contacto_aviso(self):
  contacto1 = Contacto.objects.get(id=1)
  self.assertEqual(contacto1.avisos,False)





