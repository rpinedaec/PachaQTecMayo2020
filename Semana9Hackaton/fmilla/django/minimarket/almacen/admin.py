from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_filter = ("categoria", "nombre")


admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)