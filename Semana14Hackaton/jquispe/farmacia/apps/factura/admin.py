from django.contrib import admin

from .models import DetalleFactura, Factura


class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura


class FacturaAdmin(admin.ModelAdmin):

    raw_id_fields = ('cliente',)
    inlines = (DetalleFacturaInline,)
    exclude = ['vendedor', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.vendedor = request.user
        obj.save()
admin.site.register(Factura, FacturaAdmin)