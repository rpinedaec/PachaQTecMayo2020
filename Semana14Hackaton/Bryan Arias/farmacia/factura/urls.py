from django.urls import path, include
from factura.views import index, getClientes, setPedido, getProductos
from django.contrib.auth.decorators import login_required

app_name = 'admin'

urlpatterns = [
    path('', login_required(index), name = 'index'),
    path('getClientes', getClientes),
    path('getProductos', getProductos),
    path('setPedido', setPedido),
]
