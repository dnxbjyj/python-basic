# coding:utf-8
# 执行命令行命令的三种方式
import os
import commands

command = 'ls -al /root'

def method1():
    '''
    方式1
    '''
    os.system(command)
    # 执行结果：返回执行状态码

def method2():
    '''
    方式2
    '''
    out1 = os.popen(command)
    print out1.read()
    # 输出：执行结果字符串

def method3():
    '''
    方式3
    '''
    (status,out) = commands.getstatusoutput(command)
    # 输出：status是执行状态码，out是执行结果字符串