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
    if temp > 50:
        return "小cpu的体温 %.2f°C...热死了~~" % (temp)
    return "小cpu的体温 %.2f°C...." % (temp)

#获取运行时间
def monitor_runtime():
    uptime = {}
    f = open("/proc/uptime")
    con = f.read().split()
    f.close()
    all_sec = float(con[0])
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY )
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['allminute']= int(all_sec / MINUTE)
    uptime['Free rate'] = float(con[1]) / float(con[0])
    runtime = '小语已经工作了%d天%d小时%d分。' % (uptime['day'], uptime['hour'], uptime['minute'])
    return runtime
    



