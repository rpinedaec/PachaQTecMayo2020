from django.urls import path, include
from farma.views import index, getClientes,nuevo, getTransportistas, getProductos, setProductoStock, estadoPedido, ubicacionPedido, setPedido, setTipoCliente
from django.contrib.auth.decorators import login_required

app_name = 'farma'

urlpatterns = [
    path('', login_required(index), name = 'index'), 
    path('nuevo', login_required(nuevo), name = 'nuevo'), 
    #path('/admin', login_required(admin), name = 'admin'), 
    path('getClientes', login_required(getClientes), name='getclientes'),
    path('getTransportistas', getTransportistas),
    path('getProductos', getProductos),
    path('estadoPedido/<int:idPedido>', estadoPedido),
    path('ubicacionPedido/<int:idPedido>', ubicacionPedido),
    path('setPedido', setPedido),
    path('setProductoStock', setProductoStock),
    path('setTipoCliente',login_required(setTipoCliente), name='setTipoCliente' ),
]
 