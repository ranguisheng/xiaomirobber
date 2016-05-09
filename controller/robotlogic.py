#coding:utf-8
'''
Created on 2015年12月17日

@author: 201510260176
'''

from splinter import  Browser
import time
import urllib.request
from builtins import range
from bs4 import BeautifulSoup
from  datetime  import  *  
import  sys,os,time,sched  

# today = datetime.date.today()
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep)
  
class ProcessLogic(object):
    def process(self,urlStr,timeStr):
        with Browser() as browser:
            count=100
            sleeop=1
            #vist url
            #url = "http://10.100.138.14:8383/active/toChristmasActivity.shtml?userId=100184881177"
            browser.visit(urlStr)
            #browser.fill('wd', 'splinter - python acceptance testing for web applications')
            # Find and click the 'search' button
            button = browser.find_by_id('btn_lottery')
            for i in range(1,count):
                try:
                    req = urllib.request.Request(urlStr)
                    response = urllib.request.urlopen(req)
                    source_code = response.read()
                    #print(source_code)
                    soup = BeautifulSoup(source_code,"html.parser")
                    num = soup.find('span', {'id':'number'}).string.strip() #<span id="number">0</span>
                    if num == None:
                        print("没找到对应的span")
                    if num == '0':
                        print("你没有抽奖机会了...........T_T")
                        break
                    else:
                        print("你还有%s次抽奖机会"%num)
                        print("第次%s抽奖"%i)
                        button.click()
                        
                        time.sleep(sleeop)
                except Exception as e:
                    print("看起来出现了问题%s"%e)
            browser.quit()
        print("show time after 10 seconds:") 
        timming_exe("echo %time%", 10)
def timming_exe(self,cmd, inc = 60): 
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动 
    schedule.enter(inc, 0, perform_command, (cmd, inc)) 
    # 持续运行，直到计划时间队列变成空为止 
    schedule.run()    
def perform_command(self,cmd, inc): 
    os.system(cmd)
if __name__ == '__main__':
    logic = ProcessLogic()
    logic.process('http://10.100.138.14:8383/active/toChristmasActivity.shtml?userId=100184881177','')
    pass