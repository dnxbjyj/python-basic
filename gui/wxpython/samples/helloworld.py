# coding:utf-8
# wxPython hello world程序
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # 1. 创建程序对象
    app = wx.App()
    
    # 2. 创建Frame对象
    win = wx.Frame(None,title = 'Hello World',size = (300,200))
    # 3. 在Frame对象上创建Panel面板对象
    panel = wx.Panel(win)
    # 4. 创建显示文本的区域
    text_area = wx.TextCtrl(panel, style=wx.TE_READONLY)
    # 设置文本区域值
    text_area.SetValue('Hello World!')
    # 5. 创建横向容器box
    hbox = wx.BoxSizer()
    # 6. 把文本区域放到hbox中
    hbox.Add(text_area, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=0)
    # 7. 把hbox放到面板中
    panel.SetSizer(hbox)
    
    # 8. 显示窗口
    win.Show()
    # 9. 程序主循环
    app.MainLoop()
    
if __name__ == '__main__':
    main()