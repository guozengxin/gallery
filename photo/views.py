#!/usr/bin/env python
#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
	return render_to_response('photo/index.html', context_instance=RequestContext(request))
