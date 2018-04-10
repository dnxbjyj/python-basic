# coding:utf-8
# 用wxPython实现一个最简单的文本编辑器
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Foxpad(object):
    '''
    Foxpad文本编辑器类
    '''
    def __init__(self, size = (700, 500)):
        '''
        初始化窗口
        '''
        self.__size = size
        # 创建Frame窗口对象
        self.__win = wx.Frame(None,title = "Foxpad",size = size)
        # 在窗口对象上创建Panel面板对象
        self.__bkg = wx.Panel(self.__win)
        
        # 创建"打开"按钮，用于打开文件
        self.__openBtn = wx.Button(self.__bkg, label='打开')
        # 给该按钮绑定回调函数：openFile
        self.__openBtn.Bind(wx.EVT_BUTTON, self.openFile)

        # 创建用于显示选择的文件的路径的文本区对象
        self.__filepath_area = wx.TextCtrl(self.__bkg, style=wx.TE_READONLY)
        
        # 创建"保存"按钮，用于保存对文件的修改
        self.__saveBtn = wx.Button(self.__bkg, label='保存')
        # 给该按钮绑定回调函数：saveFile
        self.__saveBtn.Bind(wx.EVT_BUTTON, self.saveFile)
        
        # 创建一个横向box，相当于一个容器
        self.__hbox = wx.BoxSizer()
        # 往横向box中添加打开文件按钮、文件路径文本区、保存文件按钮
        # proportion：控件的横向比例，为0表示自适应大小
        # flag：控件的位置参数、拉伸等属性
        # border：控件的外边距像素值
        self.__hbox.Add(self.__openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
        self.__hbox.Add(self.__filepath_area, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
        self.__hbox.Add(self.__saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)

        # 创建一个纵向box，相当于一个容器
        self.__vbox = wx.BoxSizer(wx.VERTICAL)
        # 把横向box添加到纵向box中，比例自适应
        self.__vbox.Add(self.__hbox, proportion=0, flag=wx.EXPAND | wx.ALL)
        
        # 创建用于显示文件文本内容的多行文本区对象
        self.__multiline_editor = wx.TextCtrl(self.__bkg, style=wx.TE_MULTILINE)
        # 把多行文本区添加到纵向box中，比例为1，即尽量多占
        self.__vbox.Add(self.__multiline_editor,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

        # 把纵向box放到窗口面板中
        self.__bkg.SetSizer(self.__vbox)
    def show(self):
        '''
        显示窗口
        '''
        # 显示窗口
        self.__win.Show()
    def openFile(self,evt):
        '''
        打开按钮回调函数
        '''
        # 打开系统默认风格的文件选择对话框
        dlg = wx.FileDialog(self.__win,"打开文件","","","All files (*.*)|*.*",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        filepath = ''
        # 当点击了文件选择对话框的确认按钮，给filepath变量赋值为当前选择的文件的路径；如果点击了取消按钮，不做任何操作
        if dlg.ShowModal() == wx.ID_OK:
            filepath = dlg.GetPath()
        else:
            # 当点击了取消按钮或关闭对话框按钮，什么也不做
            return
        # 设置文件路径文本区对象的值为选中的文件路径（绝对路径）
        self.__filepath_area.SetValue(filepath)
        # 打开文件，读取文件内容并显示到多行编辑区中
        with open(filepath,'r') as file:
            fcontent = file.read()
            self.__multiline_editor.SetValue(fcontent)
    def saveFile(self,evt):
        '''
        保存按钮回调函数
        '''
        # 如果当前打开的文件为空，直接返回
        if not self.__filepath_area.GetValue():
            return
        # 获取当前多行编辑区的文本内容
        fcontent = self.__multiline_editor.GetValue()
        # 把当前的文本内容写入文件
        with open(self.__filepath_area.GetValue(),'w+') as file:
            file.write(fcontent)
        # 弹出消息框，提示保存成功，消息框的样式采用"OK_DEFAULT"类型的消息框
        dlg = wx.MessageDialog(None, "保存成功！", "保存修改", wx.OK_DEFAULT)
        # 显示消息框
        dlg.ShowModal()

def main():
    # 创建程序对象
    app = wx.App()
    
    # 创建foxpad对象
    foxpad = Foxpad()
    # 显示窗口
    foxpad.show()
    
    # 程序主循环
    app.MainLoop()
    
if __name__ == '__main__':
    main()