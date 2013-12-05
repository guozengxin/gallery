#!/usr/bin/env python
#encoding=utf-8

from django.conf.urls import patterns, include, url
from photo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
)
