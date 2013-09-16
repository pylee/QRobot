# -*- coding: utf-8 -*-
import urllib
import urllib2
import os

#监视http链接
def monitor_http():
	try:
		urllib2.urlopen('http://ginsmile.github.io')
		return "http://ginsmile.github.io 神经连接正常。"
	except:
		return '错了~~您的阵地被中二君攻陷！'



