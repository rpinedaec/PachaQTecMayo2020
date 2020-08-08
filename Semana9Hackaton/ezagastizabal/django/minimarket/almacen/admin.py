from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto



class AdminLstProd(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'precio','categoria')


admin.site.register(Producto, AdminLstProd)
admin.site.register(Categoria)
# admin.site.register(Producto)
