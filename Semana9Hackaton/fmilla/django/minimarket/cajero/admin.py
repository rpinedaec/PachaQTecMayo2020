from django.contrib import admin

# Register your models here.
from .models import Factura
from .models import Cliente

class FacturaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "cliente")
    list_filter = ("fecha",)


admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cliente)