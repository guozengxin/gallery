#!/usr/bin/env python
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from g.service import db_service

# Create your views here.

def index(request):
	return render_to_response('g/index.html', context_instance=RequestContext(request))

def gallery(request):
	gallerys = db_service.get_gallerys()
	return render_to_response('g/gallery.html', {'gallerys': gallerys}, context_instance=RequestContext(request))

def topic(request):
	return render_to_response('g/topic.html', context_instance=RequestContext(request))

def slide(request):
	return render_to_response('g/slide.html', context_instance=RequestContext(request))
