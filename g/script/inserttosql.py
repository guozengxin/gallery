#!/usr/bin/env python
#encoding=utf-8

import sys
import MySQLdb
import os
import logging
import pybcs

#设置日志级别
pybcs.init_logging(logging.INFO)

AK = 'ZnzhNMuZPIGjst5pdBbRIIdG'
SK = 'hBWPV4kz9tWjA5io6599aOtksIVxHb39'
BUCKET = 'allphotos'

def main(argv):
	bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK, pybcs.HttplibHTTPC)    #这里可以显式选择使用的HttpClient, 可以是:
	b = bcs.bucket(BUCKET)
	start = 0
	lst = []
	while start == 0 or (start > 0 and len(lst) > 0):
		lst = b.list_objects(start=0, limit=1000)
		for l in lst:
			print l
		start += len(lst)


if __name__ == '__main__':
	main(sys.argv[1:])
