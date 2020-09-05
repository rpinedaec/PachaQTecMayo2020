# from Django.db import models
# from Django import forms

# class BuscarCompras(forms.Form):
#     class Meta:
#         Fecha_Inicial = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
#         Fecha_Final = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

from django import forms
from Django.db import models
from django.contrib.admin import widgets                                       


class BuscarPedido(forms.ModelForm):
       mydate = forms.DateField(widget=widgets.AdminDateWidget)
       mytime = forms.TimeField(widget=widgets.AdminTimeWidget)
       mydatetime = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
       fields = ['mydate', 'mytime', 'mydatetime']


