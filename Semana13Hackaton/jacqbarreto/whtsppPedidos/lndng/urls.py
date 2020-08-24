from django.urls import path, include
from lndng.views import index
urlpatterns = [
    path('', index)
]
