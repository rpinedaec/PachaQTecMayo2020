from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pdds.urls')),
    path('', include('lndng.urls'))
    # path('fbmssgr/', include('mssngr.urls'))
]