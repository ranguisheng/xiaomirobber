import sys
from tkinter import *
from tkinter import  messagebox
from controller.robotlogic import ProcessLogic
#sys.path.append("..")

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #定义url输入控件
        self.urlLabel = Label(self, text='请输入url:')
        self.urlLabel.pack()
        
        self.urlInput=Entry(self)
        self.urlInput.pack()
        #定义开抢时间输入控件
        self.timeLabel = Label(self, text='开抢时间:')
        self.timeLabel.pack()
        
        self.timeInput=Entry(self)
        self.timeInput.pack()
        #定义按钮
        self.allertButton = Button(self,text='确定',command=self.processParam)
        self.allertButton.pack()
        
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.quitButton.pack()
    def processParam(self):
        defaultUrl="http://10.100.138.14:8383/active/toChristmasActivity.shtml?userId=100184881177"
        urlStr=self.urlInput.get() or defaultUrl
        messagebox.showinfo('Message', 'url is:%s' % urlStr)
        logic = ProcessLogic()
        logic.process(urlStr,'')
if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('小米抢单利器')
    # 主消息循环:
    app.mainloop()