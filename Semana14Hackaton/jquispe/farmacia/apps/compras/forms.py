from .models import * # Change as necessary
from django.forms import ModelForm
from django import forms

class TodoListForm(ModelForm):
  class Meta:
    model = Cabecera
    exclude =('trabajador',)
    widgets = {
    			'codigo': forms.TextInput(attrs={'class': 'form-control'}),
				'distribuidor': forms.Select(attrs={'class': 'form-control'}),
				'laboratorio': forms.Select(attrs={'class': 'form-control'}),
				
			}



class TodoItemForm(forms.ModelForm):
	class Meta:
		model = DetalleCompra
		exclude = ('list',)
		widgets = {
				'medicamento': forms.Select(attrs={'class': 'form-control'}),
				'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
				
			}

class RangoForm (forms.Form):
    fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_i', 'data-date-format':'dd/mm/yyyy'}))
    fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_f', 'data-date-format':'dd/mm/yyyy'}))
