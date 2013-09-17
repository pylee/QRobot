# -*- coding: utf-8 -*-
import random

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

#print hello()
