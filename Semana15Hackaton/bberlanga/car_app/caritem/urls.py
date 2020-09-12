from django.urls import path
from .views import CarItem, CarItemDetails

urlpatterns=[
    path('caritem/',CarItem.as_view()),
    path('detail/<int:id>/', CarItemDetails.as_view()),
]