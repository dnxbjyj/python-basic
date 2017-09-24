# coding:utf-8
# 如何用Python装饰器实现一个函数计时器？
from functools import wraps
import time

def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        print '[Function: {name} start...]'.format(name = function.__name__)
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print '[Function: {name} finished, spent time: {time:.2f}s]'.format(name = function.__name__,time = t1 - t0)
        return result
    return function_timer

class MyTimer(object):
    '''
    用上下文管理器计时
    '''
    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '[finished, spent time: {time:.2f}s]'.format(time = time.time() - self.t0)

def test(x,y):
    s = x + y
    time.sleep(1.5)
    print 'the sum is: {0}'.format(s)

if __name__ == '__main__':
    # test(1,2)
    # 输出结果
    '''
    [Function: test start...]
    the sum is: 3
    [Function: test finished, spent time: 1.50s]
    '''

    with MyTimer() as t:
        test(1,2)
        time.sleep(1)
        print 'do other things'
    # 输出：
    '''
    the sum is: 3
    do other things
    [finished, spent time: 2.53s]
    '''