from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from autosapp import views as appviews
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()

router.register(r'tipo', appviews.TipoViewSet)
router.register(r'marca', appviews.MarcaViewSet)
router.register(r'vehiculo', appviews.VehiculoViewSet)

urlpatterns = [
    path('detalleapi',include(router.urls)),
    path('admin/', admin.site.urls),
]
