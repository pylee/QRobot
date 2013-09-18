# -*- coding: utf-8 -*-
import random
import urllib2
import json
import re

#吐槽函数
def hello(hour):
	if hour == 23:
		return "今晩は~~ご主人さま~"
	else:
		#myfile = open('../../res/greet.txt','rU')
		myfile = open('../res/greet.txt','rU')
		lines = {}
		lines = myfile.readlines()
		index = random.choice(range(len(lines) - 1))
		return lines[index]

#print hello(11)


# def getWeather():
# 	#用天气预报评论
# 	#目前仅支持秦皇岛的天气
# 	weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/101091101.html' ).read()
# 	weatherJSON = json.JSONDecoder().decode(weatherHtml)
# 	weatherInfo = weatherJSON['weatherinfo']

# 	#注意，这里从网上抓的数据返回的是unicode类型的字符串，要把它转化成urf-8
# 	weather = "今天东秦的温度为" + weatherInfo['temp1'].encode('utf-8') + "，" + weatherInfo['weather1'].encode('utf-8')+"。"
# 	return weather 

# # s = getWeather()
# # print s


#获得相应地区的天气
def getLocationWeather(location):
	location = (location.split())[-1]

	#myfile = open('../../res/weather.txt','r')
	myfile = open('../res/weather.txt','r')
	str = myfile.read() #读取的文件为utf-8编码
	tuples = re.findall(ur"([\u4e00-\u9fa5]+):(\d+)", str.decode('utf-8'))  #将utf-8编码解码成unicode
	myDic = dict(tuples) #myDic里面都是unicode编码
	try:
		print 'precessing weather code....' + location
		weatherCode = myDic[location.decode('utf-8')].encode('utf-8')
	except:
		print 'oh no~~'
		return "123"

	weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/%s.html' % (weatherCode)).read()
	weatherJSON = json.JSONDecoder().decode(weatherHtml)
	weatherInfo = weatherJSON['weatherinfo']

	#注意，这里从网上抓的数据返回的是unicode类型的字符串，要把它转化成urf-8
	weather =   "今天%s的温度为%s,%s,%s,%s" \
				%(weatherInfo['city'].encode('utf-8'), 
				weatherInfo['temp1'].encode('utf-8'),
				weatherInfo['weather1'].encode('utf-8'),
				weatherInfo['wind1'].encode('utf-8'),
				weatherInfo['index_d'].encode('utf-8'))
	return weather

#print getLocationWeather("房山区")


def comment():
	myfile = open('../res/comment.txt','rU')
	lines = {}
	lines = myfile.readlines()
	index = random.choice(range(len(lines) - 1))
	return lines[index]