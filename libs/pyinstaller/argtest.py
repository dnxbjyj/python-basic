# coding:utf-8
# 测试argparse模块的基本用法
import argparse

# 创建参数解析对象，并添加脚本用法帮助
parser = argparse.ArgumentParser(description = 'test the base usage of argparse.')

# 添加位置参数
# 所谓位置参数，就是指直接添加的参数而不用使用'-'、'--'等符号
# 添加了位置参数，它就是必选参数
parser.add_argument('arg0')

# 添加可选参数，但如果执行命令时带有该参数，后面必须跟参数值
# '-'后面跟短参数，'--'后面跟长参数
# help参数为该参数的帮助信息
parser.add_argument('-a1','--arg1',help = 'this is arg1')

# 添加可选参数，但后面不能跟参数值
parser.add_argument('-a2','--arg2',help = 'this is arg2',action = 'store_true')

# 添加可选参数并指定参数值数据类型为整型，且数据范围为[0,1,2]，且指定默认值为0,如果输入的值不是整型或值不在要求的范围内，则会报错
parser.add_argument('-a3','--arg3',type = int,choices = [0,1,2],default = 0,help = 'this is arg3')

# 添加一组可选的互斥参数
# a4和a5参数不能同时出现，否则会报错
group = parser.add_mutually_exclusive_group()
group.add_argument('-a4','--arg4',action = 'store_true')
group.add_argument('-a5','--arg5',action = 'store_true')

#####################################

# 执行解析参数
args = parser.parse_args()

# 打印出位置参数'arg0'
print 'arg0 is: ',args.arg0

# 打印出其他位置参数，注意这里要用参数的'--'名称（长参数）
if args.arg1:
    print 'arg1 is: ',args.arg1

# 因为arg2后面没有跟参数值，所以打印出来是True
if args.arg2:
    print 'arg2 is: ',args.arg2
    
if args.arg3:
    print 'arg3 is: ',args.arg3
    
if args.arg4:
    print 'arg4 is: ',args.arg4
    
if args.arg5:
    print 'arg5 is: ',args.arg5
    