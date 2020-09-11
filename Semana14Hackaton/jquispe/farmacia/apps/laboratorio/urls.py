from django.conf.urls import patterns, url
from .views import CreateLaboratorio, ListaLaboratorio, DetalleView, ActualizarView, EliminarView

urlpatterns = patterns('',		
	#clientes
	url(r'^lista_laboratorios/$', ListaLaboratorio.as_view(), name = 'lista_laboratorios'),
	url(r'^detalle_laboratorios/(?P<pk>\d+)/$', DetalleView.as_view(), name ='detalle_laboratorios'),
	url(r'^actualizar_laboratorios/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_laboratorios"), 
	url(r'^eliminar_laboratorios/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_laboratorios"), 
	url(r'^create_laboratorios/$', CreateLaboratorio.as_view(), name='create_laboratorios'),
  )