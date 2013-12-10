#!/usr/bin/env python
#encoding=utf-8

from django.conf.urls import patterns, include, url
from g import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^topic/$', views.topic, name='topic'),
	url(r'^slide/$', views.slide, name='slide'),
)
