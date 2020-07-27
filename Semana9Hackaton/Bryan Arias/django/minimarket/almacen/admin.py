from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    list_filter = ('Categoria__Nombre',)
    raw_id_fields = ('Categoria',)
    search_fields = ('Nombre', 'CategoriaAdmin__Nombre')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)