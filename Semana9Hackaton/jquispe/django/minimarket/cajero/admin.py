from django.contrib import admin
# Register your models here.
    
from .models import Cliente
from .models import Empresa
from .models import FacturaCabecera
from .models import facturaDetalle

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(FacturaCabecera)
admin.site.register(facturaDetalle)
