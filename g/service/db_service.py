#!/usr/bin/env python
#encoding=utf-8

from g.models import Gallery, Photo, Slide, Topic

def get_gallerys():
	result = []
	allphotos = Photo.objects.all()
	allgallerys = Gallery.objects.all()
	for g in allgallerys:
		r = {}
		photos = Photo.objects.filter(gallery=g)
		r['gallery'] = g
		r['photo'] = photos
		result.append(r)
	return result

