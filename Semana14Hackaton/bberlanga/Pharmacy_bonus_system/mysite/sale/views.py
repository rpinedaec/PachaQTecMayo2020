from django.shortcuts import render, redirect
from django.http import HttpResponse
from django .views.generic import TemplateView
from sale.forms import SaleForm


class Sale(TemplateView):
    template_name='sale/index.html'

    def get(self, request):
        return render(request, self.template_name)

class SetSale(TemplateView):
    template_name='sale/SetSale.html'
    
    def get(self, request):
        form=SaleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            # taxes = form.cleaned_data['taxes']
            # total_amount = form.cleaned_data['total_amount']
            # opt_payment = form.cleaned_data['opt_payment']
            # usr_id = form.cleaned_data['usr_id']
            # usr_point = form.cleaned_data['usr_point']
            # point = form.cleaned_data['point']
        args = {'form': form, 'value': form.cleaned_data['value'], 'taxes': form.cleaned_data['taxes'], 'total_amount': form.cleaned_data['total_amount'], 'opt_payment': form.cleaned_data['opt_payment'], 'usr_id': form.cleaned_data['usr_id'], 'usr_point': form.cleaned_data['usr_point'], 'point': form.cleaned_data['point'] }
        return render(request, self.template_name, args)
