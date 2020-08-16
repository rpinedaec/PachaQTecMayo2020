from django.urls import path, include
from pdds.views import index
urlpatterns = [
    path('', index),
    
]
