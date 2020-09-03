from django import forms
from sale.models import Sale
from django.utils.timezone import now

pay_type = ((1,'cash'), (2,'card'), (3,'credit card'))
in_pnt = ((1,'yes'), (0,'no'))

class SaleForm(forms.ModelForm):
    value = forms.DecimalField( max_digits=10, decimal_places=2 )
    taxes = forms.DecimalField( max_digits=10, decimal_places=2 )
    total_amount = forms.DecimalField( max_digits=10, decimal_places=2 )
    opt_payment = forms.CharField( max_length=20, widget=forms.Select(choices=pay_type) )
    usr_id = forms.CharField( max_length=20 )
    usr_point = forms.CharField( max_length=5, widget=forms.Select(choices=in_pnt))
    points = forms.DecimalField( max_digits=10, decimal_places=2 )

    class Meta:
        model = Sale 
        fields = ('value','taxes','total_amount','opt_payment','usr_id','usr_point','points')



