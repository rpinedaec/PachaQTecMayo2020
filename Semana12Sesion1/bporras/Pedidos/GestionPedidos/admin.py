from django.contrib import admin
from GestionPedidos.models import *

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("tipocliente", "tipodocumento", "nombres", "apellidos", "documento", "email", "telefono", "isActivo")
    search_fields = ("nombres", "apellidos", "documento", "email", "telefono")
    list_filter = ("tipocliente", "tipodocumento", "isActivo")

admin.site.register(tipoCliente)
admin.site.register(tipoDocumento)
admin.site.register(tipoProducto)
admin.site.register(transportista)
admin.site.register(producto)
admin.site.register(cliente, ClientesAdmin)
admin.site.register(pedido)
admin.site.register(detallePedido)

