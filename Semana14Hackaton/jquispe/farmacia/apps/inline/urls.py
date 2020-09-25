# -*- coding:utf-8 -*-
from django.conf.urls import url,patterns,include
from views import *

urlpatterns = patterns('',
        url(r'^$',todo_listListView.as_view()),
        url(r'^create/$',todo_listCreateView.as_view()),
        url(r'^update/(?P<pk>[\d]+)/$',todo_listUpdateView.as_view()),
        url(r'^(?P<pk>[\d]+)$',todo_listDetailsView.as_view()),
)

#include this file in the pattern r'^todolist/'
