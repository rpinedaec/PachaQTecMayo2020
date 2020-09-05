from django.db import models

# Create your models here.


class producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=10,decimal_places=2)

class cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    direccion = models.TextField(max_length=1000)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=10, null=True)
    puntos = models.DecimalField(max_digits=10,decimal_places=2)

class pedido(models.Model):
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    igv = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    ubicacion = models.CharField(max_length=500, null= True)
    estado = models.CharField(max_length=30,default='Recibido')

class detallePedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
