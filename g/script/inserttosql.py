#!/usr/bin/env python
#encoding=utf-8

import sys
import os
import logging
import pybcs
from datetime import date
import re
sys.path.append('/home/xiaoxin/code/git/gallery')
from g.models import Gallery, Photo

#设置日志级别
pybcs.init_logging(logging.INFO)

AK = 'ZnzhNMuZPIGjst5pdBbRIIdG'
SK = 'hBWPV4kz9tWjA5io6599aOtksIVxHb39'
BUCKET = 'allphotos'

def parsedate(datestr):
	m = re.search('(\d{4})(\d{2})(\d{2})', datestr)
	if m:
		d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
		s = d.isoformat()
		return s
	m = re.search('(\d{4})', datestr)
	if m:
		d = date(int(m.group(1)), 1, 1)
		s = d.isoformat()
		return s
	return '2010-01-01'



def insert(objname, url):
	pos1 = objname.find('/')
	pos2 = objname.find('/', pos1+1)
	if pos1 < pos2:
		foldname = objname[pos1+1:pos2]
		g = Gallery.objects.filter(name=foldname)
		if not g:
			d = parsedate(foldname)
			g = Gallery(name=foldname, date=d)
			g.save()
		else:
			g = g[0]
		(small_path, middle_path, large_path) = ('', '', '')
		if url.find('_thumb') >= 0:
			small_path = url
		elif url.find('_middle') >= 0:
			middle_path = url
		else:
			large_path = url
		objname = objname.replace('_thumb', '')
		objname = objname.replace('_middle', '')
		ps = Photo.objects.filter(name=objname)
		if not ps:
			p = Photo(name=objname, gallery = g, small_path=small_path, middle_path=middle_path, large_path=large_path, ok=False)
			p.save()
		else:
			p = ps[0]
			if small_path:
				p.small_path = small_path
			elif middle_path:
				p.middle_path = middle_path
			elif large_path:
				p.large_path = large_path
			if p.small_path and p.middle_path and p.large_path:
				p.ok = True
			p.save()

def main(argv):
	bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK, pybcs.HttplibHTTPC)    #这里可以显式选择使用的HttpClient, 可以是:
	b = bcs.bucket(BUCKET)
	sign = ();
	start = 0
	lst = []
	while start == 0 or (start > 0 and len(lst) > 0):
		lst = b.list_objects(start=start)
		for l in lst:
			objname, url = l.object_name, l.get_url
			insert(objname, url)
		start += len(lst)

if __name__ == '__main__':
	main(sys.argv[1:])
