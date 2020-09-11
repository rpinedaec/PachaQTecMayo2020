from django.db import models
from apps.medicamentos.models import Medicamentos
from apps.distribuidor.models import Distribuidor
from apps.laboratorio.models import Laboratorio
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
class TimeStampModel(models.Model):

	created = models.DateField(auto_now_add=True)
	modified = models.DateField(auto_now=True)

	class Meta:
		abstract = True



class Cabecera(TimeStampModel):	
	trabajador = models.ForeignKey(settings.AUTH_USER_MODEL)
	codigo = models.CharField(max_length=10, unique=True)
	distribuidor = models.ForeignKey(Distribuidor)
	laboratorio = models.ForeignKey(Laboratorio)
	fecha = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.codigo
		



class DetalleCompra(models.Model):
	list=models.ForeignKey(Cabecera, related_name='cabecera')
	medicamento=models.ForeignKey(Medicamentos)
	cantidad=models.IntegerField(max_length=9)

	def suma(self):
		return self.cantidad * self.medicamento.precio_Compra




	def __unicode__(self):
		return unicode(self.medicamento)

def update_stock(sender, instance, **kwargs):
	instance.medicamento.stock += instance.cantidad
	instance.medicamento.save()

# register the signal
signals.post_save.connect(update_stock, sender=DetalleCompra, dispatch_uid="update_stock_count")
