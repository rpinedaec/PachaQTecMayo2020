from django.urls import path, include
from administración.views import index, getClientes, getProductos, estadoPedido, ubicacionPedido, setPedido, setTipoCliente
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name = 'index'),
    path('getClientes', getClientes),
    path('getProductos', getProductos),
    path('estadoPedido/<int:idPedido>', estadoPedido),
    path('ubicacionPedido/<int:idPedido>', ubicacionPedido),
    path('setPedido', setPedido),
    path('setTipoCliente',login_required(setTipoCliente), name='setTipoCliente' ),
]