"""hrkprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hrkprj.quickstart import views
from hrkapp import views as hrkappViews
from rest_framework import routers
# from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'artista', hrkappViews.ArtistaViewSet, basename = 'artista')
router.register(r'album', hrkappViews.AlbumViewSet, basename = 'album')
router.register(r'cancion', hrkappViews.CancionViewSet, basename = 'cancion')
router.register(r'user', hrkappViews.UserViewSet, basename = 'user')
router.register(r'playlist', hrkappViews.PlaylistViewSet, basename = 'playlist')
router.register(r'cancionplaylist', hrkappViews.CancionDePlaylistViewSet, basename = 'canciondeplaylist')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

