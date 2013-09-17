# -*- coding: utf-8 -*-
import time
import random
from tools import login
from tools import greet
from tools import monitor
from tools import loadpic


def run():
    client = login.login()
    lastid = 0
    inter = 100 #检查间隔

   
    while True:
        inter += 1 #加1秒
        now = time.strftime('%M%S',time.localtime(time.time()))
        hour = time.strftime('%H',time.localtime(time.time()))

        #由于weibo API限制，不能发布自己可见微博，所以我设置了一个密友可见，密友就是我自己的另外一个账号，用来监控cpu温度和运行时间
        if now == '0430':
            print "sending a monitor weibo"
            monitor_info = monitor.monitor_cpu_temp()
            monitor_info += monitor.monitor_runtime()
            monitor_info += monitor.monitor_http()
            try:
                client.statuses.update.post(status=monitor_info, visible = 2)
            except:
                pass

        #发微
        if now == '4600' and hour in ['07', '12', '11', '17','18', '22','23']:
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
            
            if random.choice(range(2)):
                content = '%s' %(greeting)
            else:
                content = '%s%s' %(greeting, monitor_info)
            try:
                #随机选择发图或者不发图,1/3可能性发图
                if random.choice(range(3)):
                    client.statuses.update.post(status=content)
                else:
                    client.statuses.upload.post(status=content, pic = myPic)                
            except:
                pass 
            myPic.close()

            print "Send succesfully!"
            time.sleep(1)

        #对最新 @我 的原创微博进行评论,50s一次
        if inter > 50:
            try:
                #获取原创的最新微博的id
                mentions = client.statuses.mentions.get(since_id = lastid, filter_by_type = 1)
                for weiboInfo in mentions['statuses']:
                    lastid = weiboInfo['id']
                    print lastid
                    myComment = greet.getComment() #取得秦皇岛天气
                    client.comments.create.post(id = lastid, comment = myComment)
                    print 'comment successfully! id:%d comment:%s' %(lastid, myComment)
            except Exception, e:
                print e
                pass
            inter = 0

        time.sleep(1)



if __name__=="__main__":
    run()
