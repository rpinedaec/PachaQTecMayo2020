from django.contrib import admin
from apps.compras.models import DetalleCompra, Cabecera


class medicamento_compraInline(admin.TabularInline):
    model = DetalleCompra

class compraAdmin(admin.ModelAdmin):
    inlines = (medicamento_compraInline,)

admin.site.register(Cabecera, compraAdmin)