#encoding:utf-8
from django import forms
from .models import Medicamentos, Presentacion


class MedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos
		exclude = ('lote',)

		widgets = {			
			'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
			'precio_Compra': forms.NumberInput(attrs={'class': 'form-control'}),
			'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'id':'valor3'}),
			'presentacion': forms.Select(attrs={'class': 'form-control'}),
			'tipo': forms.Select(attrs={'class': 'form-control'}),
			'fecha_expiracion': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
			'fecha_produccion': forms.DateInput(attrs={'class':'form-control', 'id':'Date1', 'data-date-format':'dd/mm/yyyy'}),
			'igv': forms.NumberInput(attrs={'class': 'form-control', 'id':'total'}),
			}

class CrearmedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos

		widgets = {
				'lote': forms.TextInput(attrs={'class': 'form-control'}),
				'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'precio_Compra': forms.NumberInput(attrs={'class': 'form-control', 'id': 'precio_compra'}),
				'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'id':'precio_venta'}),
				'presentacion': forms.Select(attrs={'class': 'form-control'}),
				'tipo': forms.Select(attrs={'class': 'form-control'}),
				'fecha_expiracion': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
				'fecha_produccion': forms.DateInput(attrs={'class':'form-control', 'id':'Date1', 'data-date-format':'dd/mm/yyyy'}),
				'igv': forms.NumberInput(attrs={'class': 'form-control', 'id':'igv'}),
			}


class CrearpresentacionForm(forms.ModelForm):
		class Meta:
			model = Presentacion
			widgets = {
				'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			}
