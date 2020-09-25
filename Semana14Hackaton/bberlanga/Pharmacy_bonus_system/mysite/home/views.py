from django.shortcuts import render, redirect
from django.http import HttpResponse
from django .views.generic import TemplateView

class Home(TemplateView):
    template_name='home/index.html'

    def get(self,request):
        return render(request, self.template_name)