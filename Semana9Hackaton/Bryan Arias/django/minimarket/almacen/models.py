from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nombre = models.CharField(max_length=50)
    
class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Stock = models.IntegerField(default=0)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
