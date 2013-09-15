# -*- coding: utf-8 -*-
import weibo
import time
import random
import urllib
import urllib2
import os
from weibo import APIClient
import config.myConfig as u

#吐槽函数
def greet():
	myfile = open('greet.txt','rU')
	lines = {}
	lines = myfile.readlines()
	index = random.choice(range(len(lines) - 1))
	return lines[index]

#网站监控函数 
def monitor():

	try:
		urllib2.urlopen('http://ginsmile.github.io')
		return "主页 http://ginsmile.github.io 访问良好"
	except:
		return '杯具了，被墙了？'

def run():
    #login
    client = APIClient(app_key = u.APP_KEY, app_secret = u.APP_SECRET, redirect_uri = u.CALLBACK_URL)
    referer_url = client.get_authorize_url()
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)

    postdata = {
             "client_id": u.APP_KEY,
             "redirect_uri": u.CALLBACK_URL,
             "userId": u.USERID,
             "passwd": u.PASSWD,
             "isLoginSina": "0",
             "action": "submit",
             "response_type": "code",
             }
 
    headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
               "Host": "api.weibo.com",
               "Referer": referer_url
               }
 
    req  = urllib2.Request(
                           url = referer_url,
                           data = urllib.urlencode(postdata),
                           headers = headers
                           )
    try:
        resp = urllib2.urlopen(req)
        #获取最后32个字符
        code=resp.geturl()[-32:]
        #通过该code获取access_token，r是返回的授权结果
        r = client.request_access_token(code)  
        #将access_token和expire_in设置到client对象
        client.set_access_token(r.access_token, r.expires_in)
    except Exception, e:
        print 'oh no'
        print e

    monitor_info = monitor()
    greeting = greet()
    content = ''
    if random.choice([0,1]) == 1:
    	content = '%s %s' %(greeting, monitor_info)
    else:
    	content = '%s' %(greeting)

    client.statuses.update.post(status=content)  
    print "Send succesfully!"
    time.sleep(1)

if __name__=="__main__":
	run()
