#!/usr/bin/env python
#encoding=utf-8

import Image
import os

def make_thumb_width(path, width=250, suffix='_thumb'):
	'''
	生成缩略图
	'''
	img = Image.open(path)
	w, h = img.size
	if w <= width:
		pass
	elif w > width:
		h = int(float(width) / w * h)
		w = width

	thumb = img.resize((w, h), Image.ANTIALIAS)
	base, ext = os.path.splitext(path)
	filename = base + suffix + ext
	thumb.save(filename, quality=100)
	return filename

def test():
	f = '/media/本地磁盘/download/photo/lwj/2011/IMG_5740.JPG'
	make_thumb_width(f)

if __name__ == '__main__':
	test()

