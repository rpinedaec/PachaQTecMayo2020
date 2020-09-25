from django.urls import path
from .import views

urlpatterns=[
    path('create_account',views.Create_account.as_view(),name='customer'),
    path('log_in',views.LogIn.as_view(),name='log_in'),
    path('profile/<int:idnumber>/',views.Profile.as_view(),name='profile')
]