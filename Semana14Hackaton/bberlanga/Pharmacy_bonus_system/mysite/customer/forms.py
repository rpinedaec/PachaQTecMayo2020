from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    id_number=forms.CharField()
    name = forms.CharField(label='nombre', widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    last_name = forms.CharField()
    usr_name = forms.CharField()
    usr_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = Customer 
        fields = ('id_number','name','last_name','usr_name','usr_password')

class LoginForm(forms.Form):
    id_number = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

