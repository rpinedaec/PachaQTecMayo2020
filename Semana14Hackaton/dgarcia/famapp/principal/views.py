from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'latest_question_list': 1,
    }
    return render(request, 'principal/index.html', context)