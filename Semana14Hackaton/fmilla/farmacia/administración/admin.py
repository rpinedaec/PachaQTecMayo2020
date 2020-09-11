from django.contrib import admin
from .models import tipoCliente, tipoDocumento, tipoProducto, producto, cliente


class tipoClienteAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'isActivo')


class tipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'isActivo')


class tipoProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'isActivo')


class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipoproducto', 'igv', 'costo', 'isActivo')


class clienteAdmin(admin.ModelAdmin):
    list_display = ('tipocliente', 'tipodocumento', 'nombres',
                    'apellidos', 'documento', 'email', 'telefono', 'isActivo')



admin.site.register(producto, productoAdmin)
admin.site.register(cliente, clienteAdmin)
admin.site.register(tipoDocumento, tipoDocumentoAdmin)
admin.site.register(tipoProducto, tipoProductoAdmin)
admin.site.register(tipoCliente, tipoClienteAdmin)