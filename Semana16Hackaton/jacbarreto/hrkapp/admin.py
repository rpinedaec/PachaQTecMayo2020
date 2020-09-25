from django.contrib import admin
from .models import *

# Register your models here.
class ArtistaAdmin(admin.ModelAdmin):
    #readonly_fields=('created', 'updated')
    column = ('artista')
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album', 'artista')
class CancionAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'album')
class TipomusicaAdmin(admin.ModelAdmin):
    column = ('tipomusica')
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('catalogo','tipomusica','cancion')
class UsuarioAdmin(admin.ModelAdmin):
    column = ('nombre')
class PlaylistAdmin(admin.ModelAdmin):
     list_display = ('playlist','catalogo','nombre')


admin.site.register(artista, ArtistaAdmin)
admin.site.register(album, AlbumAdmin)
admin.site.register(cancion, CancionAdmin)
admin.site.register(tipomusica, TipomusicaAdmin)
admin.site.register(catalogo, CatalogoAdmin)
admin.site.register(usuario, UsuarioAdmin)
admin.site.register(playlist, PlaylistAdmin)

