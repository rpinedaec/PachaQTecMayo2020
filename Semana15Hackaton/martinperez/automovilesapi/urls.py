
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from automoviles import views as autoViews

from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter() 
router.register(r'tipo',autoViews.TipoViewSet, basename='descripcion') 
router.register(r'marca',autoViews.MarcaViewSet, basename='descripcion') 
router.register(r'automovil',autoViews.AutomovilViewSet, basename='descripcion')
router.register(r'automovil',autoViews.AutomoviPorMarcaViewSet, basename='marca')
router.register(r'automovil',autoViews.AutomoviPorTipoViewSet, basename='tipo')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
 