from django.contrib import admin

# Register your models here.
from .models import Periodo
from .models import Transaccion
from .models import Consolidado_actividades

admin.site.register(Periodo)
admin.site.register(Transaccion)
admin.site.register(Consolidado_actividades)