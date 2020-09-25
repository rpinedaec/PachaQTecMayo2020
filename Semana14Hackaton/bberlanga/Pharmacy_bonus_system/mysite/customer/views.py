from django.shortcuts import render, redirect
from django.http import HttpResponse
from django .views.generic import TemplateView
from customer.forms import CustomerForm
from customer.forms import LoginForm
from customer.models import Customer

class Create_account(TemplateView):
    template_name='customer/create_account.html'

    def get(self, request):
        form=CustomerForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            usr_name = form.cleaned_data['usr_name']
            usr_password = form.cleaned_data['usr_password']
        args = {'form': form, 'name': name, 'last_name': last_name, 'usr_name': usr_name, 'usr_password': usr_password}
        return render(request, self.template_name, args)

class LogIn(TemplateView):
    template_name = 'customer/log_in.html'

    def get(self, request):
        form=LoginForm()
        return render(request,self.template_name, {'form': form})
    
    def post(self, request):
        id_num = request.POST['id_number']
        user = Customer.objects.get( id_number = id_num )
        password = user.usr_password
        if password == request.POST['password']:   
            return redirect(f'/customer/profile/{id_num}')
        else:
            return redirect( '/customer/log_in')


class Profile(TemplateView):
    template_name = 'customer/profile.html'
    
    def get( self, request, idnumber ):        
        customer = Customer.objects.get( id_number = idnumber )
        args = {'customer': customer}      
        return render(request, self.template_name, args)