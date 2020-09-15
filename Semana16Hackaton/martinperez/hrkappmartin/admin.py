 
from django.contrib import admin
from hrkappmartin.models import Pelicula ,artista,cancion,album,playlist

class peliculaAdmin(admin.ModelAdmin):
    list_display = ('code', 'year', 'name', 'created' )

class artistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'direccion', 'telefono', 'email', 'actividadPrincipal', 'activo')

class cancionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'artista', 'activo' )

class albumAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cancion', 'activo' ) 

class playlistAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'cancion', 'activo' ) 


admin.site.register(Pelicula, peliculaAdmin)
admin.site.register(artista, artistaAdmin)
admin.site.register(cancion, cancionAdmin)
admin.site.register(album, albumAdmin)
admin.site.register(playlist, playlistAdmin)