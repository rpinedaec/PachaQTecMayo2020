from django.shortcuts import render
from apps.distribuidor.models import Distribuidor
from .forms import DistribuidorForm
from braces.views import LoginRequiredMixin,GroupRequiredMixin
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
# Create your views here.

class ListaDistribuidor(LoginRequiredMixin,GroupRequiredMixin, ListView):
	context_object_name = 'distribuidores'
	model = Distribuidor
	template_name = 'distribuidores/lista_distribuidores.html'
	group_required = ['trabajadores']


# Create your views here.
class DetalleView(LoginRequiredMixin, DetailView):
	model = Distribuidor
	template_name = 'distribuidores/detalle_distribuidores.html'


class ActualizarView(UpdateView):
	form_class = DistribuidorForm
	template_name = 'distribuidores/create_update_distribuidores.html'
	model = Distribuidor
	success_url='/lista_distribuidores'



class EliminarView(GroupRequiredMixin, DeleteView):
	model = Distribuidor
	success_url='/lista_distribuidores'
	template_name = 'distribuidores/eliminar_distribuidores.html'
	group_required = ['administrador']



class CreateDistribuidor(LoginRequiredMixin, CreateView):
	form_class = DistribuidorForm
	template_name = 'distribuidores/create_update_distribuidores.html'
	model = Distribuidor
	success_url = '/lista_distribuidores'