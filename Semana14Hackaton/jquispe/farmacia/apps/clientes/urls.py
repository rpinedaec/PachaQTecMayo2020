from django.conf.urls import patterns, url
from .views import CreateCliente, ListaCliente, DetalleView, ActualizarView, EliminarView

urlpatterns = patterns('',		
	#clientes
	url(r'^lista_clientes/$', ListaCliente.as_view(), name = 'lista_clientes'),
	url(r'^detalle_cliente/(?P<pk>\d+)/$', DetalleView.as_view(), name ='detalle_cliente'),
	url(r'^actualizar_clientes/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_clientes"), 
	url(r'^eliminar_cliente/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_cliente"), 
	url(r'^create_clientes/$', CreateCliente.as_view(), name='create_clientes'),
  )