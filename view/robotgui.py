from tkinter import *
from tkinter import  messagebox

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
        self.allertButton = Button(self,text='确定',command=self.hello)
        self.allertButton.pack()
        
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.quitButton.pack()
    def hello(self):
        name=self.urlInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello,%s' % name)
app = Application()
# 设置窗口标题:
app.master.title('小米抢单利器')
# 主消息循环:
app.mainloop()