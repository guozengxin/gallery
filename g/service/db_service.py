#!/usr/bin/env python
#encoding=utf-8

import random
from g.models import Gallery, Photo, Slide, Topic

def get_gallerys():
	result = []
	allgallerys = Gallery.objects.all()
	for g in allgallerys:
		r = {'nahe':g.name, 'p_preview':[]}
		photos = Photo.objects.filter(gallery=g, ok=True)[:4]
		i = random.randint(-15,15)
		for p in photos:
			r['p_preview'].append({'url':p.small_path, 'degree':str(i%15)+'deg'})
			i += 10
		result.append(r)
	return result

def photo_by_gname(gname):
	result = {}
	g = Gallery.objects.filter(name=gname)
	result = {'name': g[0].name, 'description': g[0].description, 'photos':[]}
	photos = Photo.objects.filter(gallery=g, ok=True)
	for p in photos:
		r = {}
		r['middle_path'] = p.middle_path
		r['small_path'] = p.small_path
		result['photos'].append(r)
	return result

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
		return ps
