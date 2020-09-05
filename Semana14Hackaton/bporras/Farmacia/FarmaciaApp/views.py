from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'FarmaciaApp/home.html')

def tienda(request):
    return render(request,'FarmaciaApp/tienda.html')

def blog(request):
    return render(request,'FarmaciaApp/blog.html')

def contacto(request):
    return render(request,'FarmaciaApp/contacto.html')
