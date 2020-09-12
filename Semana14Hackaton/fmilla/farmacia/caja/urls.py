from django.urls import path
from caja.views import index
urlpatterns = [
    path('', index)
]