from django.contrib import admin
from .models import cliente, tipoDocumento, uMedida, categoria, tipoProducto, producto, vendedor, tipoCliente

class tipoClienteAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'isActivo')


class tipoDocumentoAdmin(admin.ModelAdmin):
    column_name = ('descripcion')

class clienteAdmin(admin.ModelAdmin):
    list_display = ('tipocliente','tipodocumento', 'nombre', 'apellidos', 'documento',
                        'direccion', 'email', 'telefono', 'puntos')
   
class tipoProductoAdmin(admin.ModelAdmin):
    column_name = ('descripcion')


class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'igv', 'presentacion', 'fechavenc', 'existenciainic',
                     'entradas', 'salidas', 'stock', 'umedida', 'categoria', 'tipoproducto')

class uMedidaAdmin(admin.ModelAdmin):
    list_display = ('sigla','descripcion')

class categoriaAdmin(admin.ModelAdmin):
    column_name = ('descripcion')
    
class vendedorAdmin(admin.ModelAdmin):
    list_display = ('dni', 'codigo', 'nombre', 'apellidos')

admin.site.register(tipoCliente, tipoClienteAdmin)
admin.site.register(tipoDocumento, tipoDocumentoAdmin)
admin.site.register(cliente, clienteAdmin)
admin.site.register(tipoProducto, tipoProductoAdmin)
admin.site.register(producto, productoAdmin)
admin.site.register(uMedida, uMedidaAdmin)
admin.site.register(categoria, categoriaAdmin)
admin.site.register(vendedor, vendedorAdmin)
