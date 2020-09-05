#encoding:utf-8
from django import forms
from .models import Laboratorio

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Laboratorio