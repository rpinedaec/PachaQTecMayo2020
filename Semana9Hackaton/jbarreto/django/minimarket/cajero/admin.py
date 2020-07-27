from django.contrib import admin

# Register your models here.
from .models import Cliente
from .models import Cab_comprobantepago
from .models import Det_comprobantepago

admin.site.register(Cliente)
admin.site.register(Cab_comprobantepago)
admin.site.register(Det_comprobantepago)