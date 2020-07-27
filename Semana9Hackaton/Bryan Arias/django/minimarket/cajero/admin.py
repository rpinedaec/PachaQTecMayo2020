from django.contrib import admin

# Register your models here.
from .models import Cliente
from .models import Documento
from .models import Factura

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('Descripcion',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    list_filter = ('Tipo_Documento__Descripcion',)
    search_fields = ('Nombre', )
    raw_id_fields = ('Tipo_Documento', )
    filter_horizontal = ('Factura',)
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'get_prod', 'Cantidad', 'Fecha')
    list_filter = ('Cliente__Nombre', 'Producto__Nombre', 'Fecha')
    date_hierarchy = 'Fecha'
    ordering = ('-Fecha',)
    search_fields = ('Cliente__Nombre', 'Producto__Nombre')
    raw_id_fields = ('Cliente', 'Producto')

    def get_name(self, obj):
        return obj.Cliente.Nombre
    get_name.admin_order_field  = 'Nombre'  #Allows column order sorting
    get_name.short_description = 'Nombre Cliente'  #Renames column head

    def get_prod(self, obj):
        return obj.Producto.Nombre
    get_prod.admin_order_field  = 'Nombre'  #Allows column order sorting
    get_prod.short_description = 'Nombre Producto'  #Renames column head

admin.site.register(Documento, DocumentoAdmin)    
admin.site.register(Cliente, ClienteAdmin)  
admin.site.register(Factura, FacturaAdmin)

