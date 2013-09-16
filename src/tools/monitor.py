# -*- coding: utf-8 -*-
import urllib2
import os

#监视http链接
def monitor_http():
	try:
		urllib2.urlopen('http://ginsmile.github.io')
		return "http://ginsmile.github.io 神经连接正常。"
	except:
		return '打不开了~~您的阵地被中二君攻陷！'

#监视cpu温度
def monitor_cpu_temp():
    temp =  float(os.popen('vcgencmd measure_temp').readline().replace("temp=","").replace("'C\n",""))
    return "小cpu的体温 %.2f°C" % (temp)
    



