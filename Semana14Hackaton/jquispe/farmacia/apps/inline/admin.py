from django.contrib import admin
from models import *
# Register your models here.
class todolistAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(todo_list,todolistAdmin)