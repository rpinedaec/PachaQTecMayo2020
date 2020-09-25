from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from authenticate.views import Login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pdds.urls')),
    path('', include('lndng.urls')),
    path('fbmssgr/', include('mssngr.urls')),
    path('tlgrm/',  include('tlgrm.urls')),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'), 
    path('accounts/login/', Login.as_view(), name = 'login'),
]