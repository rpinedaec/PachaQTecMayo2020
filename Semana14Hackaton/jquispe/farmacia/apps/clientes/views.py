# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from .models import Cliente
from .forms import ClienteForm
from braces.views import LoginRequiredMixin,GroupRequiredMixin

class ListaCliente(LoginRequiredMixin,GroupRequiredMixin, ListView):
	context_object_name = 'clientes'
	model = Cliente
	template_name = 'clientes/lista_cliente.html'
	group_required = ['trabajadores']


# Create your views here.
class DetalleView(LoginRequiredMixin, DetailView):
	model = Cliente
	template_name = 'clientes/detalle_clientes.html'


class ActualizarView(UpdateView):
	form_class = ClienteForm
	template_name = 'clientes/create_update_clientes.html'
	model = Cliente
	success_url='/lista_clientes'



class EliminarView(GroupRequiredMixin, DeleteView):
	model = Cliente
	success_url='/lista_clientes'
	template_name = 'clientes/eliminar_cliente.html'
	group_required = ['administrador']



class CreateCliente(LoginRequiredMixin, CreateView):
	form_class = ClienteForm
	template_name = 'clientes/create_update_clientes.html'
	model = Cliente
	success_url = '/lista_clientes'