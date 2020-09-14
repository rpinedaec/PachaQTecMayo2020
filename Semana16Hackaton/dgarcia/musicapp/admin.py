from django.contrib import admin

from musicapp.models import Artista

class artistaAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_favorite', 'created', 'modified' )

admin.site.register(Artista, artistaAdmin)


