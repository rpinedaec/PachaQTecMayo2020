from django import forms

class FormularioTipoProducto(forms.Form):
    descripcion = forms.CharField()
    estado = forms.CharField()
