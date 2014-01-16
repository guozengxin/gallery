#!/usr/bin/env python
#coding:utf8

import os
import logging
import pybcs

#设置日志级别
pybcs.init_logging(logging.INFO)


# 请修改这里
#AK = os.environ['ZnzhNMuZPIGjst5pdBbRIIdG']           #请改为你的AK
#SK = os.environ['hBWPV4kz9tWjA5io6599aOtksIVxHb39']         #请改为你的SK
AK = 'ZnzhNMuZPIGjst5pdBbRIIdG'
SK = 'hBWPV4kz9tWjA5io6599aOtksIVxHb39'
BUCKET = 'allphotos'

lastfile = '/20130907/IMG_9705.JPG'
begin = False

def upload(name, path, b):
	global begin
	for f in os.listdir(path):
		objname = '/' + name + '/' + f
		f = os.path.join(path, f)
		if objname == lastfile:
			print 'ok'
			begin = True
		if os.path.isfile(f) and begin:
			retry = 3
			while retry > 0:
				o = b.object(objname)
				try:
					o.put_file(f)
					succ = True
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
	basedir = '/home/xiaoxin/code/git/gallery/all-photos/'
	for name in  os.listdir(basedir):
		path = os.path.join(basedir, name)
		if os.path.isdir(path):
			upload(name, path, b)




if __name__ == '__main__':
	main()

