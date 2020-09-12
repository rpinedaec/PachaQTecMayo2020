from django.urls import path, include
from principal.views import index
urlpatterns = [
    path('', index)
]
