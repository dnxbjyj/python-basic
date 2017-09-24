# coding:utf-8
# sorted函数的三种用法
from operator import itemgetter

data1 = [{'aa':22,'bb':11},{'aa':12,'cc':23},{'aa':67,'dd':103}]
data2 = [{'age':18,'name':'Tom'},{'age':10,'name':'Tim'},{'age':30,'name':'John'},{'age':18,'name':'Amy'}]

def sort1():
    # 对data1依据'aa'字段值的大小从小打到排序
    ret = sorted(data1,key = lambda item:item['aa'])  # 注：如果这里的key写'bb'或'cc'，会报KeyError，因为这两个属性并不是每个元素都有的
    print ret
    # 输出：
    '''
    [{'aa': 12, 'cc': 23}, {'aa': 22, 'bb': 11}, {'aa': 67, 'dd': 103}]
    '''

def sort2():
    # 对data1依据'aa'字段值的大小从小打到排序
    ret = sorted(data1,cmp = lambda x,y:cmp(x['aa'],y['aa']))
    print ret
    # 输出：
    '''
    [{'aa': 12, 'cc': 23}, {'aa': 22, 'bb': 11}, {'aa': 67, 'dd': 103}]
    '''

def sort3():
    # 使用itemgetter对data1依据'aa'字段值的大小从小打到排序
    ret = sorted(data1,key = itemgetter('aa'))
    print ret
    # 输出：
    '''
    [{'aa': 12, 'cc': 23}, {'aa': 22, 'bb': 11}, {'aa': 67, 'dd': 103}]
    '''

def sort4():
    # 对data2进行排序，先按照'age'从小到大排序，'age'相同的情况下，再按照'name'排序
    ret = sorted(data2,key = itemgetter('age','name'))
    print ret
    # 输出：
    '''
    [{'age': 10, 'name': 'Tim'}, {'age': 18, 'name': 'Amy'}, {'age': 18, 'name': 'Tom'}, {'age': 30, 'name': 'John'}]
    '''

if __name__ == '__main__':
    sort4()