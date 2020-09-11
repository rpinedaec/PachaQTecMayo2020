from django.contrib import admin
from apps.ventas.models import todo_item, Cabecera_Venta


class medicamento_ventaInline(admin.TabularInline):
    model = todo_item

class Detalle_VentaAdmin(admin.ModelAdmin):
    inlines = (medicamento_ventaInline,)

admin.site.register(Cabecera_Venta, Detalle_VentaAdmin)