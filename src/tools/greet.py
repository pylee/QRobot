# -*- coding: utf-8 -*-
import random
import urllib2
import json

#吐槽函数
def hello(hour):
	if hour == 23:
		return "今晩は~~ご主人さま~"
	else:
		myfile = open('../../res/greet.txt','rU')
		#myfile = open('../res/greet.txt','rU')
		lines = {}
		lines = myfile.readlines()
		index = random.choice(range(len(lines) - 1))
		return lines[index]

#print hello(11)


def getComment():
	#用天气预报评论
	#目前仅支持秦皇岛的天气
	weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/101091101.html' ).read()
	weatherJSON = json.JSONDecoder().decode(weatherHtml)
	weatherInfo = weatherJSON['weatherinfo']

	weather = weatherInfo['city'] + "," + weatherInfo['date_y'] + "," +  weatherInfo['temp1'] + "."
	return weather

	
#print getComment()