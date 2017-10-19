# coding:utf-8
# 选择目录Demo
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tkinter
from tkinter import StringVar,Tk,Label,Entry,Button
from tkinter.filedialog import askdirectory

# 设置一个路径对象
path = None

def select_path():
    '''
    选择路径回调函数
    :return: None
    '''
    global path
    _path = askdirectory()
    path.set(_path)


def main():
    global path

    # 创建顶层窗口
    root = Tk()
    # 必须在创建顶层窗口后，才能初始化path
    path = StringVar()

    # 设置界面元素
    label = Label(root,text = '目标路径：').grid(row = 0,column = 0)
    entry = Entry(root,textvariable = path).grid(row = 0,column = 1)
    btn = Button(root,text = '选择路径',command = select_path).grid(row = 0,column = 2)

    # 点击按钮，在命令行中显示最新的文件路径
    btn_show_path = Button(root,text = '显示文件路径',command = show_path).grid(row = 2,column = 1)

    # 事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()