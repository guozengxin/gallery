#!/usr/bin/env python
#encoding=utf-8

from g.models import Gallery, Photo, Slide, Topic

def get_gallerys():
	allgallerys = Gallery.objects.all()
	return allgallerys

def photo_by_gname(gname):
	g = Gallery.objects.filter(name=gname)
	photos = Photo.objects.filter(gallery=g, ok=True)
	return photos

def delete_photo(pname):
	print pname
	ps = Photo.objects.filter(name=pname)
	for p in ps:
		p.ok = False
		p.save()

def save_info(pname, topic, desc, labels):
	ps = Photo.objects.filter(name=pname)
	if len(ps) > 0:
		p = ps[0]
		p.labels = labels
		p.desc = desc
		p.save()
		return 'success'
	return 'fail'

def search_info(pname):
	ps = Photo.objects.filter(name=pname)
	info = {}
	if len(ps) > 0:

