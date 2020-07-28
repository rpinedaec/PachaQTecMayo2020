from django.urls import path
from . import views  # . este punto significa que estamos en el mismo directorio

urlpatterns = [
    path('', views.home, name="miniMarket-Home"),
    path('about/', views.about, name="miniMarket-About")

]
