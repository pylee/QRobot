# -*- coding: utf-8 -*-
import time
import random
from tools import login
from tools import greet
from tools import monitor
from tools import loadpic


def run():
    client = login.login()
   
    while True:
        now = time.strftime('%M%S',time.localtime(time.time()))
        hour = time.strftime('%H',time.localtime(time.time()))

        #整点检查,相应小时的11分，运行
        if now == '1111'and hour in (7, 11, 12, 17, 18, 21, 23):
            monitor_info = ""
            if random.choice(range(3)):
                monitor_info += monitor.monitor_cpu_temp()
            else:
                monitor_info += monitor.monitor_http()

            greeting = ""
            greeting += greet.hello(hour)
            myPic = loadpic.pic()
            
            if random.choice(range(4)):
                content = '%s' %(greeting)
            else:
                content = '%s%s' %(greeting, monitor_info)
            try:
                #随机选择发图或者不发图,1/4可能性发图
                if random.choice(range(4)):
                    client.statuses.update.post(status=content)
                else:
                    client.statuses.upload.post(status=content, pic = myPic)                
            except:
                pass 
            myPic.close()

            print "Send succesfully!"
            time.sleep(1)

        time.sleep(1)



if __name__=="__main__":
    run()
