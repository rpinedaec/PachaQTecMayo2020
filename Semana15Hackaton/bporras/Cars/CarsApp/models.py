from django.db import models

# Create your models here.


class Marca(models.Model):
    marca = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'marca'
        verbose_name_plural=  'marcas'
    def __str__(self):
        return self.marca

class Tipo(models.Model):
    tipo = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'tipo'
        verbose_name_plural=  'tipos'
    def __str__(self):
        return self.tipo

class Auto(models.Model):
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    año = models.PositiveSmallIntegerField()
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name= 'auto'
        verbose_name_plural=  'autos'
    def __str__(self):
        return self.modelo
