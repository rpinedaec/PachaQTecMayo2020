from django.contrib import admin
from apps.medicamentos.models import Presentacion, Medicamentos


@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
	list_display = ('nombre',  )

@admin.register(Medicamentos)
class MedicamentosAdmin(admin.ModelAdmin):
	list_display = ('lote', 'presentacion', 'nombre', 'descripcion', 'fecha_expiracion', 'fecha_produccion', 'tipo', 'precio_Compra','precio_venta', 'stock')
	search_fields = ('nombre', 'descripcion')
