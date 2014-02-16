#!/usr/bin/env python
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson

from g.service import db_service

# Create your views here.

def index(request):
	return render_to_response('g/index.html', context_instance=RequestContext(request))

# gallery标签下的操作
def gallery(request):
	'''
	查询所有相册信息
	'''
	gallerys = db_service.get_gallerys()
	return render_to_response('g/gallery.html', {'gallerys': gallerys}, context_instance=RequestContext(request))

def gallery_photo_by_gname(request):
	'''
	根据相册名查询照片信息，返回相册浏览的页面元素
	方法: get
	参数: gname(相册名)
	'''
	gname = request.GET.get('gname', None)
	photos = db_service.photo_by_gname(gname)
	return render_to_response('g/photo-list.html', {'photos': photos, 'gname':gname}, context_instance=RequestContext(request))

def gallery_detail(request):
	'''
	根据相册名查询照片信息，返回相册浏览的大图页面
	方法: get
	参数: gname(相册名)
	'''
	gname = request.GET.get('gname', None)
	photos = db_service.photo_by_gname(gname)
	return render_to_response('g/gallery-detail.html', {'photos': photos}, context_instance=RequestContext(request))

def gallery_delete_photo(request):
	'''
	根据照片名删除照片
	方法: post
	参数: pname(照片名)
	'''
	pname = request.POST.get('pname', None)
	print pname
	if pname:
		db_service.delete_photo(pname)
	return HttpResponse('')

def gallery_save_info(request):
	'''
	保存照片信息
	'''
	pname = request.POST.get('pname', None)
	topic = request.POST.get('topic', None)
	desc = request.POST.get('desc', None)
	labels = request.POST.get('labels', None)
	message = db_service.save_info(pname, topic, desc, labels)
	return HttpResponse(simplejson.dumps({'message': message}))

def gallery_search_info(request):
	'''
	根据照片名查询照片信息
	'''
	pname = request.POST.get('pname', None)
	photo_info = db_service.search_info(pname)
	return HttpResponse(simplejson.dumps({'succeed': True, 'photo-info': photo_info}))

# topic标签下的页面
def topic(request):
	return render_to_response('g/topic.html', context_instance=RequestContext(request))

def slide(request):
	return render_to_response('g/slide.html', context_instance=RequestContext(request))
