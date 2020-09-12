from django.conf.urls import patterns, url
from .views import CreateDistribuidor, ListaDistribuidor, DetalleView, ActualizarView, EliminarView

urlpatterns = patterns('',		
	#clientes
	url(r'^lista_distribuidores/$', ListaDistribuidor.as_view(), name = 'lista_distribuidores'),
	url(r'^detalle_distribuidores/(?P<pk>\d+)/$', DetalleView.as_view(), name ='detalle_distribuidores'),
	url(r'^actualizar_distribuidores/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_distribuidores"), 
	url(r'^eliminar_distribuidor/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_distribuidor"), 
	url(r'^create_distribuidor/$', CreateDistribuidor.as_view(), name='create_distribuidor'),
  )