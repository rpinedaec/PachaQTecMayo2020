from django.conf.urls import patterns, url
from .views import Home

urlpatterns = patterns('',
	url(r'^$', 'apps.users.views.userlogin', name="login"),
	url(r'^salir/$', 'apps.users.views.LogOut', name = 'logout'),
#principal
	url(r'^home', Home.as_view(), name='home'),
)