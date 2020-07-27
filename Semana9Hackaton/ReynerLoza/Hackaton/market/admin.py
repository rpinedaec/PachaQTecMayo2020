from django.contrib import admin

# Register your models here.

from .models import Productos
from .models import Categoria
admin.site.register(Categoria)
admin.site.register(Productos)
