from django.db import models
# para que se vea reflejado a nuestro current timezone
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaCreacion = models.DateTimeField(default=timezone.now)
    # auto_now => used more when this Producto is updated
    # auto_now_add=> when the Product is created but you we cant updated it any more
    # default => aca con timezone.now podemos tener la habilidad de cambiarlo mas adelante
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
