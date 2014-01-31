#!/usr/bin/env python
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from g.service import db_service

# Create your views here.

def index(request):
	return render_to_response('g/index.html', context_instance=RequestContext(request))

# gallery标签下的页面
def gallery(request):
	gallerys = db_service.get_gallerys()
	return render_to_response('g/gallery.html', {'gallerys': gallerys}, context_instance=RequestContext(request))

def gallery_photo_by_gname(request):
	gname = request.GET.get('gname', None)
	result = ''
	if gname is None:
		result = '<p>参数错误</p>'
	photos = db_service.photo_by_gname(gname)
	return render_to_response('g/photo-list.html', {'photos': photos}, context_instance=RequestContext(request))

def gallery_detail(request):
	gname = request.GET.get('gname', None)
	photos = db_service.photo_by_gname(gname)
	return render_to_response('g/gallery-detail.html', {'photos': photos}, context_instance=RequestContext(request))

# topic标签下的页面
def topic(request):
	return render_to_response('g/topic.html', context_instance=RequestContext(request))

def slide(request):
	return render_to_response('g/slide.html', context_instance=RequestContext(request))
