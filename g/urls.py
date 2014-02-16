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
	url(r'^gallery/photo-by-gname$', views.gallery_photo_by_gname, name='gallery-photo-by-gname'),
	url(r'^gallery/detail/$', views.gallery_detail, name='gallery-detail'),
	url(r'^gallery/delete-photo$', views.gallery_delete_photo, name='gallery-delete-photo'),
	url(r'^gallery/save-info$', views.gallery_save_info, name='gallery-save-info'),
	url(r'^gallery/search-info$', views.gallery_search_info, name='gallery-search-info'),

	url(r'^topic/$', views.topic, name='topic'),
	url(r'^slide/$', views.slide, name='slide'),
)
