from django.contrib import admin
from .models import *

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class MarcaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class TipoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Auto, AutoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Tipo, TipoAdmin)
