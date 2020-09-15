from django.db import models

# Create your models here.

class Modelo(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class Marca(models.Model):
    descripcion = models.CharField(max_length=100)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Auto(models.Model):    
    descripcion = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    color = models.CharField(max_length = 50)

    def __str__(self):
        return self.descripcion
    