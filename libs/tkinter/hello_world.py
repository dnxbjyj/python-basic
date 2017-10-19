# coding:utf-8
# tkinter库HelloWorld Demo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tkinter
from tkinter import Tk,Label

def main():
    # 创建顶层窗口
    top = Tk()

    # 设置窗口标题
    top.wm_title('Hello')

    # 在top上创建4个标签对象，并分别指定行、列位置
    Label(top,text = 'Hello World').grid(row = 0,column = 0)
    Label(top, text = 'Hello Python').grid(row = 0,column = 1)
    Label(top, text = 'Hello Tkinter').grid(row = 0,column = 2)
    Label(top, text='你好！').grid(row = 1,column = 1)

    # 执行主循环，显示GUI
    tkinter.mainloop()

if __name__ == '__main__':
    main()