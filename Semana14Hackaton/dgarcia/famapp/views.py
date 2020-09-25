from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'FarmApp/home.html')

def tienda(request):
    return render(request,'FarmApp/tienda.html')

def blog(request):
    return render(request,'FarmApp/blog.html')

def contacto(request):
    return render(request,'FarmApp/contacto.html')
