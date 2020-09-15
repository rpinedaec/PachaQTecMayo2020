
from django.contrib import admin
from .models import Song, Singer, Albun, Playlist, User

class SongAdmin(admin.ModelAdmin):

    list_display = ('musicname','id')

class SingerAdmin(admin.ModelAdmin):

    list_display = ('descripcion','idSong')

class AlbunAdmin(admin.ModelAdmin):

    list_display = ('descripcion','idSinger')

class PlaylistAdmin(admin.ModelAdmin):

    list_display = ('descripcion','idAlbum')
    
class UserAdmin(admin.ModelAdmin):
    
    list_display = ('name','lastname','idPlaylist')

# Register your models here.

admin.site.register(Song,SongAdmin)
admin.site.register(Singer,SingerAdmin)
admin.site.register(Albun,AlbunAdmin)
admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(User,UserAdmin)