from django.contrib import admin
from apps.distribuidor.models import Distribuidor


@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'ruc')
	search_fields = ('codigo', 'nombre')
