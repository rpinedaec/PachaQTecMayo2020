from django.db import models

# Create your models here.

class Modelo(models.Model):
    descripcion = models.CharField(max_length=100)

class Marca(models.Model):
    descripcion = models.CharField(max_length=100)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

class Auto(models.Model):    
    descripcion = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    color = models.CharField(max_length = 50)
    