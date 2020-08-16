from django.contrib import admin
from .models import tipoClientes, tipoDocumentos, tipoProductos, productos, clientes, transportistas

admin.site.register(transportistas)
admin.site.register(productos)
admin.site.register(clientes)
admin.site.register(tipoDocumentos)
admin.site.register(tipoProductos)
admin.site.register(tipoClientes)

# Register your models here.
