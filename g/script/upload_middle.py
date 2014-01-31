#!/usr/bin/env python
#encoding=utf-8

import os
import logging
import pybcs
import sys
sys.path.append('.')
from service import image_service

#设置日志级别
pybcs.init_logging(logging.INFO)

# 请修改这里
#AK = os.environ['ZnzhNMuZPIGjst5pdBbRIIdG']           #请改为你的AK
#SK = os.environ['hBWPV4kz9tWjA5io6599aOtksIVxHb39']         #请改为你的SK
AK = 'ZnzhNMuZPIGjst5pdBbRIIdG'
SK = 'hBWPV4kz9tWjA5io6599aOtksIVxHb39'
BUCKET = 'allphotos'

def upload(name, path, b):
	for f in os.listdir(path):
		f = os.path.join(path, f)
		if os.path.isfile(f):
			if f.find('middle') != -1 or f.find('thumb') != -1:
				continue
			middlefile = image_service.make_thumb_width(f, width=1680, suffix='_middle')
			objname = '/' + name + '/' + os.path.basename(middlefile)
			retry = 3
			while retry > 0:
				try:
					o = b.object(objname)
					pybcs.logger.info(middlefile)
					o.put_file(middlefile)
					break
				except:
					pass
				retry -= 1

def main():
	bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK, pybcs.HttplibHTTPC)    #这里可以显式选择使用的HttpClient, 可以是:
																			#HttplibHTTPC
																			#PyCurlHTTPC
	#lst = bcs.list_buckets()
	b = bcs.bucket(BUCKET)
	#lst = b.list_objects()
	basedir = '/media/本地磁盘/download/photo/lwj'
	for name in os.listdir(basedir):
		path = os.path.join(basedir, name)
		if os.path.isdir(path):
			upload(name, path, b)




if __name__ == '__main__':
	main()

