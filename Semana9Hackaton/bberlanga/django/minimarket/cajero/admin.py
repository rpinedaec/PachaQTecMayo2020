from django.contrib import admin

# Register your models here.
from .models import Metodo_pago
from .models import Detalle_factura
from .models import Factura

admin.site.register(Metodo_pago)
admin.site.register(Detalle_factura)
admin.site.register(Factura)