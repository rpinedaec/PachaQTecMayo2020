from django.contrib import admin
from movies.models import Pelicula

class peliculaAdmin(admin.ModelAdmin):
    list_display = ('code', 'year', 'name', 'created' )

admin.site.register(Pelicula, peliculaAdmin)