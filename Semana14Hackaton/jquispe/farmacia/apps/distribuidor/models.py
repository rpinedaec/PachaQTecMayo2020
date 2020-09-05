from django.db import models

class Distribuidor(models.Model):	
	nombre = models.CharField(max_length=20)	
	ruc = models.IntegerField(unique=True)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=60)

	def __unicode__(self):
		return self.nombre
