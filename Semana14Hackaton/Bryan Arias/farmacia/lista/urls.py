from django.urls import path, include
from lista.views import lista
urlpatterns = [
    path('', lista)
]
