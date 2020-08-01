from django.contrib import admin

# Register your models here.
from .models import Cajero
from .models import Cliente
from .models import FacturaCabecera
from .models import FacturaDetalle

admin.site.register(Cajero)
admin.site.register(Cliente)
admin.site.register(FacturaCabecera)
admin.site.register(FacturaDetalle)
