from django.contrib import admin
from .models import *
# Register your models here.

class TipoAdmin(admin.ModelAdmin):
    pass

class MarcaAdmin(admin.ModelAdmin):
    pass

class VehiculoAdmin(admin.ModelAdmin):
    pass

admin.site.register(tipo,TipoAdmin)
admin.site.register(marca,MarcaAdmin)
admin.site.register(vehiculo,VehiculoAdmin)