# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response 
from django.shortcuts import render_to_response as render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView
from django.core import serializers
from django.db import connection
import json
# Create your views here.
from .models import Factura, DetalleFactura
from apps.clientes.models import Cliente
from apps.medicamentos.models import Medicamentos
from django.db import transaction
from django.contrib import messages
from django.views.generic import ListView
from django.template import RequestContext as ctx
from datetime import datetime

#reporte pdf
from django.http import HttpResponseRedirect
from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import cgi

from .forms import RangoForm


@login_required
@transaction.atomic
def facturaCrear(request):

    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print proceso
            if 'serie' not in proceso:
                msg = 'Ingrese serie'
                raise Exception(msg)

            if 'numero' not in proceso:
                msg = 'Ingrese numero'
                raise Exception(msg)

            if 'clienProv' not in proceso:
                msg = 'El cliente no ha sido seleccionado'
                raise Exception(msg)

            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)

            total = 0

            for k in proceso['producto']:
                producto = Medicamentos.objects.get(id=k['serial'])
                subTotal = (producto.precio_venta) * int(k['cantidad'])
                total += subTotal

            crearFactura = Factura(
                serie=proceso['serie'],
                numero=proceso['numero'],

                cliente=Cliente.objects.get(id=proceso['clienProv']),
                fecha=timezone.now(),
                total=total,
                vendedor=request.user
            )
            crearFactura.save()
            print "Factura guardado"
            print crearFactura.id
            for k in proceso['producto']:
                producto = Medicamentos.objects.get(id=k['serial'])
                crearDetalle = DetalleFactura(
                    producto=producto,
                    descripcion=producto.nombre,
                    precio = producto.precio_venta,
                    cantidad=int(k['cantidad']),
                    impuesto=producto.igv* int(k['cantidad']),
                    subtotal=producto.precio_venta * int(k['cantidad']),
                    factura = crearFactura,
                    )
                crearDetalle.save()

            messages.success(
                request, 'La venta se ha realizado satisfactoriamente')
        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    return render_to_response('factura/crear_factura.html', {'form': form}, context_instance=RequestContext(request))

# Busqueda de clientes para factura


def buscarCliente(request):
    idCliente = request.GET['id']
    cliente = Cliente.objects.filter(dni__contains=idCliente)
    data = serializers.serialize(
        'json', cliente, fields=('dni', 'nombre', 'direccion', 'telefono'))
    return HttpResponse(data, content_type='application/json')


# Busqueda de producto para factura
def buscarProducto(request):
    idProducto = request.GET['id']
    producto = Medicamentos.objects.filter(nombre__contains=idProducto)
    data = serializers.serialize(
        'json', producto, fields=('code','stock', 'nombre', 'precio_venta', 'categoria', 'igv'))
    return HttpResponse(data, content_type='application/json')

def consultarFactura(request):
    factura = None
    detalles = None
    sum_subtotal = 0
    sum_tax = 0
    if request.method == 'POST':
        serie = request.POST.get('serie')
        numero = request.POST.get('num')

        factura = Factura.objects.get(serie=serie, numero=numero)
        detalles = DetalleFactura.objects.filter(factura=factura)

        for d in detalles:

            sum_tax = sum_tax + d.impuesto
        sum_subtotal = factura.total-sum_tax

    return render_to_response('factura/imprimir_factura.html',
                              {'factura': factura, 'detalles': detalles,
                                  'sum_subtotal': sum_subtotal, 'sum_tax': sum_tax},
                              context_instance=RequestContext(request))


class ListaVentas(ListView):
    template_name = 'factura/lista_venta.html'
    model = Factura

    def get_context_data(self, **kwargs):
        context = super(ListaVentas, self).get_context_data(**kwargs)
        context['events'] =Factura.objects.filter(vendedor=self.request.user)
        context['compras'] = context['events']
        context['paginate_by']=context['events']
        return context

def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))

@login_required(login_url='/login')
def generar_pdf(request):
    factura = Factura.objects.all()

    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        vendedor = request.POST.get('vendedor')
        
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = Factura.objects.filter(fecha__range=(fecha_in, fecha_fi)).filter(vendedor__pk=request.user.id)
          
            total = 0
            for expe in rango:
                total = ((expe.total) + (total))

            return write_pdf ('factura/reporte_factura.html',{'pagesize' : 'legal', 'rango' : rango, 'total': total})
            #return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render_to_response('factura/rango_reporte.html', {'error': error}, context_instance=RequestContext(request))

    return render_to_response('factura/rango_reporte.html', {'rangoform': RangoForm()}, context_instance=RequestContext(request))


def reporteventas(request, pk):
    compra = Factura.objects.get(pk=pk)
    medicamentos = compra.factura.all()
    hora = datetime.today()

    return render('factura/reporte_venta.html', locals(), context_instance=ctx(request))
