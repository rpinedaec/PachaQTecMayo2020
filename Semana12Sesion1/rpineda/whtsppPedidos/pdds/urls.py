from django.urls import path, include
from pdds.views import index, getClientes, getTransportistas, getProductos
urlpatterns = [
    path('', index),
    path('getClientes', getClientes),
    path('getTransportistas', getTransportistas),
    path('getProductos', getProductos),
]
