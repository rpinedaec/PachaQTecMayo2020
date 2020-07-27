from django.contrib import admin

# Register your models here.

from .models import venta, factura

admin.site.register (factura)
admin.site.register(venta)

