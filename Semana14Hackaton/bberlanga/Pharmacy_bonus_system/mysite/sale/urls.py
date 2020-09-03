from django.urls import path
from .import views

urlpatterns=[
    path('',views.Sale.as_view(),name='sale'),
    path('setsale',views.SetSale.as_view(),name='setsale')
]