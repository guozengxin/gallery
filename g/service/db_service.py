#!/usr/bin/env python
#encoding=utf-8

from g.models import Gallery, Photo, Slide, Topic

def get_gallerys():
	allgallerys = Gallery.objects.all()
	return allgallerys

def photo_by_gname(gname):
	g = Gallery.objects.filter(name=gname)
	photos = Photo.objects.filter(gallery=g, type='TI')
	oriphotos = Photo.objects.filter(gallery=g, type='OI')
	result = []
	for p in photos:
		oriname = p.name.replace('_thumb', '')
		op = oriphotos.filter(name=oriname)
		if len(op) > 0:
			r = {'name':p.name, 'oriname':oriname, 'path':p.path}
			r['oripath'] = op[0].path
			r['gallery_id'] = p.gallery_id
			r['gname'] = gname
			r['description'] = p.description
			r['labels'] = p.labels
			result.append(r)

	return result

