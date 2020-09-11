from django.config.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from tienda import views
urlpatterns = [
    url(r'^tienda/$', views.TiendaList.as_view()),
    url(r'^tienda/')
]


admin
