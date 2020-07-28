from django.contrib import admin

# Register your models here.

from .models import Administrador

admin.site.register(Administrador)


# class Productos(models.Model):
#     # define which columns displayed in changelist
#     list_display = ('id', 'nombre', 'stock', 'precio','categoria_id')
#     # add filtering by date
#     list_filter = ('categoria_id')


# admin.site.register(Productos, CommentAdmin)