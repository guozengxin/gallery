#!/usr/bin/env python
#encoding=utf-8

import sys
import MySQLdb

def main(argv):
	while True:
		line = sys.stdin.readline()
		if not line:
			break
		arr = line.split('\t')

if __name__ == '__main__':
	main(sys.argv[1:])
