# coding:utf-8
import wx

# 程序对象
app = wx.App()
# 窗口对象
win = wx.Frame(None,title="Foxpad",size=(410, 335))

# 窗口的平台
bkg = wx.Panel(win)
 
# 打开文件事件回调函数
def openFile(evt):
  # 打开文件选择框（系统默认的）
  dlg = wx.FileDialog(win,"打开文件","","","All files (*.*)|*.*",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
  filepath = ''
  # 当点击了确认按钮，给filepath变量赋值为当前选择的文件的路径；如果点击了取消按钮，不做任何操作
  if dlg.ShowModal() == wx.ID_OK:
    filepath = dlg.GetPath()
  else:
    return
  # 设置文件名文本区对象的值为选中的文件路径（绝对路径）
  filename_area.SetValue(filepath)
  # 打开文件，把文件内容显示到多行编辑区中
  with open(filepath,'r') as file:
    fcontent = file.read()
    multiline_editor.SetValue(fcontent)
 
# 保存文件事件回调函数
def saveFile(evt):
  # 如果当前打开的文件为空，直接返回
  if not filename_area.GetValue():
    return
  # 获取当前多行编辑区的文件内容
  fcontent = multiline_editor.GetValue()
  # 把最新的文件内容写入文件
  with open(filename_area.GetValue(),'w+') as file:
    file.write(fcontent)
  # 弹出消息框，提示保存成功
  dlg = wx.MessageDialog(None, "保存成功！", "保存修改", wx.OK_DEFAULT)
  dlg.ShowModal()

# 打开文件按钮
openBtn = wx.Button(bkg, label='open')
# 绑定该按钮的事件是：openFile
openBtn.Bind(wx.EVT_BUTTON, openFile)

# 保存文件按钮
saveBtn = wx.Button(bkg, label='save')
# 绑定该按钮的事件是：saveFile
saveBtn.Bind(wx.EVT_BUTTON, saveFile)

# 显示当前选择的文件的文件名文本区对象
filename_area = wx.TextCtrl(bkg, style=wx.TE_READONLY)
# 多行编辑区对象
multiline_editor = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)

# 创建一个横向box
hbox = wx.BoxSizer()
# 往横向box中添加打开文件按钮、文件名文本区、保存文件按钮
# proportion：控件的横向比例，为0表示合适大小\
# flag：控件的位置参数、拉伸等属性
# border：控件的外边距
hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
hbox.Add(filename_area, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
hbox.Add(saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)

# 纵向box
vbox = wx.BoxSizer(wx.VERTICAL)
# 把横向box添加到纵向box中
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)
# 把多行编辑区添加到纵向box中
vbox.Add(multiline_editor,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

# 把纵向box设置到bkg
bkg.SetSizer(vbox)
# 显示窗口
win.Show()
# 启动程序
app.MainLoop()