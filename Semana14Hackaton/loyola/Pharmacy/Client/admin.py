from django.contrib import admin

from .models import status, document, clientInfo

admin.site.register(status)
admin.site.register(document)
admin.site.register(clientInfo)
