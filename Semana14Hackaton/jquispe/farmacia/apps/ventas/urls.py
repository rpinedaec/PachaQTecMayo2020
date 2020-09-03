from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
	url(r'^$',todo_listCreateView.as_view()),
	url(r'^author-ajax/$', 'app.views.TodoitemAjax'),
	)
