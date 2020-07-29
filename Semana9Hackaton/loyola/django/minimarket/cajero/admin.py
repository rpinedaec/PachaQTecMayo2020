from django.contrib import admin

# Register your models here.
from .models import MetodoPago
from .models import Factura

admin.site.register(MetodoPago)
admin.site.register(Factura)