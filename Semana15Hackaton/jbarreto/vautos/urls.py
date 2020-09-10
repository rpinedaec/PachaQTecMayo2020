from django.urls import include, path
from rest_framework import routers
from vautos.quickstart import views
from pedidos import views as pedidosViews
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categoria', pedidosViews.CategoriaViewSet, basename = 'categoria')
router.register(r'marca', pedidosViews.MarcaViewSet, basename = 'marca')
router.register(r'modelo', pedidosViews.ModeloViewSet,basename = 'modelo')
router.register(r'tipoAuto', pedidosViews.TipoAutoViewSet,basename = 'tipoAuto')
router.register(r'auto',pedidosViews.AutoViewSet, basename = 'auto')

# router.register(r'tipoCliente', pedidosViews.TipoClienteViewSet, basename = 'tipoCliente')
# router.register(r'tipoProducto', pedidosViews.TipoProductoViewSet, basename = 'tipoProducto')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/some-protected-view/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    

]