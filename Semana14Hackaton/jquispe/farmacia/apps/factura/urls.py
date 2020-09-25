from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
	url(r'factura/lista_ventas/$', ListaVentas.as_view(), name = 'lista_ventas'),

	url(r'^factura/venta$', 'apps.factura.views.facturaCrear',
        name="factura_venta"),
    url(r'^factura/buscar_cliente$', 'apps.factura.views.buscarCliente'),
    url(r'^factura/buscar_producto$', 'apps.factura.views.buscarProducto'),

    url(r'^factura/consultar$', 'apps.factura.views.consultarFactura', name="consultar_factura"),


    url (r'factura/generar_reporte_factura/$', generar_pdf, name = 'generar_reporte_factura'),

    url(r'factura/reporte_ventas/(?P<pk>\d+)/$', 'apps.factura.views.reporteventas', name='reporte_ventas'),

   )
