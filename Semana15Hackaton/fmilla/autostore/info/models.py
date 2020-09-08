from django.db import models

# Create your models here.
class marca(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre = models.CharField(max_length=200)

class modelo(models.Model):
    def __str__(self):
        return f"{self.nombre}"
    nombre = models.CharField(max_length=200)

class tipo(models.Model):
    def __str__(self):
        return f"{self.descripcion}"
    descripcion = models.CharField(max_length=200)

class auto(models.Model):
    def __str__(self):
        return f"{self.codigo}, {self.marca}, {self.modelo}, {self.tipo}"
    codigo = models.IntegerField()
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(modelo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)