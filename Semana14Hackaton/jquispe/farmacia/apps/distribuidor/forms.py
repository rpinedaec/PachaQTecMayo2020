#encoding:utf-8
from django import forms
from apps.distribuidor.models import Distribuidor

class DistribuidorForm(forms.ModelForm):
	class Meta:
		model = Distribuidor
	
	nombre = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Nombre Distribuidor',
		'size': '40'}))	
	ruc = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'RUC',
		'size': '40'}))
	telefono = forms.IntegerField(widget=forms.TextInput(attrs={
		'placeholder':'Télefono',
		'size': '8'}))	
	direccion = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Dirección',
		'size': '40'}))	
