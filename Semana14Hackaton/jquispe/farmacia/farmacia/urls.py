"""mibotica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, patterns, url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    #PRODUCTOS
    path('/',include('apps.medicamentos.urls', namespace="medicamentos_app")),
    #LOGIN-USERS
    path('/', include('apps.users.urls', namespace='users_app')),
    #CLIENTES
    path('/', include('apps.clientes.urls', namespace='clientes_app')),
    #DISTRIBUIDORES
    path('/', include('apps.distribuidor.urls', namespace='distribuidores_app')),
    #COMPRAS
    path('/', include('apps.compras.urls', namespace='compras_app')),
    #LABORATORIO
    path('/', include('apps.laboratorio.urls', namespace='laboratorios_app')),
    path('todolist/', include('apps.inline.urls', namespace='todolist')),
    #FACTURA
    url('/', include('apps.factura.urls', namespace='factura_app')),
    #AGREGAR VENTAS
    path('ventas/',include('apps.ventas.urls', namespace="ventas_app")),
]

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}),)

