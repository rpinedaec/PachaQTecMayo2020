from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'market/home.html')

    #HttpResponse('<h1>Blog Home</h1>')

# Create your views here.


def about(request):

    return render(request, 'market/about.html')


# Django shortcut to render more direct way
