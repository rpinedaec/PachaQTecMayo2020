from django.contrib import admin

# Register your models here.

from .models import Clientes
from .models import Compras 


admin.site.register(Clientes)
admin.site.register(Compras) 

