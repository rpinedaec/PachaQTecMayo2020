from django.urls import path, include
from pdds.views import index, getClientes, getTransportistas, getProductos, estadoPedido, ubicacionPedido, setPedido, nuevo
urlpatterns = [
    path('', index, name="index"),
    path('nuevo', nuevo, name="nuevo"),
    path('getClientes', getClientes),
    path('getTransportistas', getTransportistas),
    path('getProductos', getProductos),
    path('estadoPedido/<int:idPedido>', estadoPedido),
    path('ubicacionPedido/<int:idPedido>', ubicacionPedido),
    path('setPedido', setPedido, name="guardar")
]
