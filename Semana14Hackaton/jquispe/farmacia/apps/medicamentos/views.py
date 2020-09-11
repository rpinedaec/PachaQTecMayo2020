# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Medicamentos, Presentacion
from .forms import MedicamentoForm, CrearmedicamentoForm, CrearpresentacionForm
from django.http import HttpResponse
import csv


#reporte pdf
from django.http import HttpResponseRedirect
from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import cgi

class ListaMedicamentos(ListView):
	context_object_name = 'medicamentos'
	model = Medicamentos
	template_name = 'medicamentos/lista_medicamentos.html'

class DetalleView(DetailView):
	model = Medicamentos
	template_name = 'medicamentos/detalle_medicamentos.html'

class ActualizarView(UpdateView):
	form_class = CrearmedicamentoForm
	template_name = 'medicamentos/create_update_medicamentos.html'
	model = Medicamentos
	success_url='/medicamentos'

class CreateMedicamentos(CreateView):
	form_class = CrearmedicamentoForm
	template_name = 'medicamentos/create_update_medicamentos.html'
	model = Medicamentos
	success_url = '/medicamentos'

class EliminarView(DeleteView):
	model = Medicamentos
	success_url='/medicamentos'
	template_name = 'medicamentos/eliminar_medicamento.html'


def CargaAtenciones_ant(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="atenciones.csv"'
	registrants= Medicamentos.objects.all()
	writer = csv.writer(response,delimiter="|")
	writer.writerow(['id','codigo','categoria','tipo','nombre','componente','concentracion','sanitario','fecha_expiracion','fecha_produccion','descripcion','precio_Compra','precio_venta','stock'])
	for registrant in registrants:
		writer.writerow([registrant.id, 
                            registrant.codigo, 
                            registrant.categoria,
                            registrant.tipo,
                            registrant.nombre.encode('utf-8'),
                            registrant.componente.encode('utf-8'),
                            registrant.concentracion.encode('utf-8'),
                            registrant.sanitario,
                            registrant.fecha_expiracion,
                            registrant.fecha_produccion,
                            registrant.descripcion.encode('utf-8'),
                            registrant.precio_Compra,
                            registrant.precio_venta,
                            registrant.stock
                            ])
	return response


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


def generar_reporte_medicamentos(request):
	 medicamentos = Medicamentos.objects.all()

	 total_precio_compra = 0
	 for expe in medicamentos:
	 	total_precio_compra = (expe.stock*expe.precio_Compra) + total_precio_compra

	 total_precio_venta = 0
	 for expe in medicamentos:
	 	total_precio_venta = (expe.stock*expe.precio_venta) + total_precio_venta

	 ganancia = total_precio_venta - total_precio_compra


	 return write_pdf ('medicamentos/reporte_detalle_medicamentos.html',{'pagesize' : 'legal',
	 				   'medicamentos' : medicamentos, 'total_precio_compra': total_precio_compra,
	 				   'total_precio_venta':total_precio_venta, 'ganancia': ganancia})

#Presentación

class CreatePresentacion(CreateView):
	form_class = CrearpresentacionForm
	template_name = 'medicamentos/create_update_presentacion.html'
	model = Presentacion
	success_url = '/medicamentos/agregar'