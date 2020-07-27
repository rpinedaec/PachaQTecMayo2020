from django.contrib import admin

# Register your models here.

from .models import Clientes
from .models import Factura
from .models import FacturasProductos


admin.site.register(Clientes)
admin.site.register(Factura)
admin.site.register(FacturasProductos)
