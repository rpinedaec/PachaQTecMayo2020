from django.db import models

# Create your models here.
class Administrador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)