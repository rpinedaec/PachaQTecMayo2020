from django.db import models
from django.utils import timezone

#NOTA: "models.Model" indica a Djngo, que la clase será guardada en la base de datos
# Create your models here.
class TipoVehiculo(models.Model):
    #Tipo de vehiculo
    descripcion = models.CharField(max_length=100)

class MarcaVehiculo(models.Model):
    #Nombre de la marca
    descripcion = models.CharField(max_length=100)
    #Modelo de la marca
    modelo = models.CharField(max_length=20)

class Vehiculo(models.Model):
	#Tipo del vehiculo
    id_Tipo_Vehiculo = models.ForeignKey('TipoVehiculo',on_delete=models.CASCADE)
	#Marca del vehiculo
    id_Marca_Vehiculo = models.ForeignKey('MarcaVehiculo',on_delete=models.CASCADE)
    #Numero de serie que identifica al vehiculo
    numero_serie = models.CharField(max_length = 80)
    #Precio del vehiculo
    precio = models.FloatField()
    #Permite determinar una representacion en string del objeto empleado
    def __str__(self):
        return self.numero_serie