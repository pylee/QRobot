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

        #由于weibo API限制，不能发布自己可见微博，所以我设置了一个密友可见，密友就是我自己的另外一个账号，用来监控cpu温度和运行时间
        if now == '4400':
            print "sending a monitor weibo"
            monitor_info = monitor.monitor_cpu_temp()
            monitor_info += monitor.monitor_runtime()
            monitor_info += monitor.monitor_http()
            try:
                client.statuses.update.post(status=monitor_info, visible = 2)
            except:
                pass

        #整点检查,相应小时的11分，运行
        if now == '4410' and hour in ['07', '09', '10', '12', '17', '18', '21', '22','23']:
            print 'sending a normal weibo'
            monitor_info = ""
            if random.choice(range(2)):
                monitor_info += monitor.monitor_cpu_temp()
            elif random.choice(range(2)):
                monitor_info += monitor.monitor_http()
            else:
                monitor_info += monitor.monitor_runtime()

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
