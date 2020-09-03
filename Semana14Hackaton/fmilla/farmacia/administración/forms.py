from django import forms
from .models import tipoCliente

class tipoClienteForm(forms.ModelForm):
    class Meta:
        model = tipoCliente
        fields = ['descripcion', 'isActivo']