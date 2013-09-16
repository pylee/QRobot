# -*- coding: utf-8 -*-
import time
import random
from tools import login
from tools import greet
from tools import monitor


def run():
    #登陆
    client = login.login()
   
    while True:
        now = time.strftime('%M%S',time.localtime(time.time()))

        #整点检查
        if now == '4159':
            monitor_info = ""
            monitor_info += monitor.monitor_http()
            greeting = ""
            greeting += greet.hello()
            
            
            content = '%s。%s' %(greeting, monitor_info)
            try:
                client.statuses.update.post(status=content) 
            except:
                pass 
            print "Send succesfully!"
            time.sleep(1)

        time.sleep(1)



if __name__=="__main__":
    run()
