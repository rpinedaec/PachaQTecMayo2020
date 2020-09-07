from django.urls import path, include
from pdds.views import index
#from pdds.views import index, getClientes, getProductos, getVendedor, estadoPedido, ubicacionPedido, setPedido, setTipoCliente
from pdds.views import index, getClientes, getProductos, getVendedor, setPedido, setTipoCliente
from django.contrib.auth.decorators import login_required

app_name = 'pedidos'

urlpatterns = [
    path('', login_required(index), name = 'index'),
    path('getClientes', getClientes),
    #path('getTransportistas', getTransportistas),
    path('getProductos', getProductos),
    #path('estadoPedido/<int:idPedido>', estadoPedido),
    #path('ubicacionPedido/<int:idPedido>', ubicacionPedido),
    path('setPedido', setPedido),
    path('setTipoCliente',login_required(setTipoCliente), name='setTipoCliente' ),

]
