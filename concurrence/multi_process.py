# coding:utf-8
# 测试多进程
import os
import time
from multiprocessing import Process,Pool,Queue
from utils import fn_timer
import random

# 简单的任务
@fn_timer
def do_simple_task(task_name):
    print 'Run child process {0}, task name is: {1}'.format(os.getpid(),task_name)
    time.sleep(1.2)
    return task_name

@fn_timer
# 1. 测试简单的多进程
def test_simple_multi_process():
    p1 = Process(target=do_simple_task, args=('task1',))
    p2 = Process(target=do_simple_task, args=('task2',))
    print 'Process will start...'
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'Process end.'

@fn_timer
# 2. 测试使用进程池
def test_use_process_pool():
    # 创建一个进程池，数字表示一次性同时执行的最大子进程数
    pool = Pool(5)
    # 任务返回值列表
    results = []
    # 任务名称列表
    task_names = []
    for i in range(7):
        task_names.append('task{0}'.format(i))
    # 并发执行多个任务，并获取任务返回值
    results = pool.map_async(do_simple_task,task_names)
    print 'Many processes will start...'
    pool.close()
    pool.join()

    print 'All processes end, results is: {0}'.format(results.get())

# 写进程执行的任务
def write(q):
    for value in ['A','B','C']:
        print 'Put value: {0} to queue.'.format(value)
        q.put(value)
        time.sleep(random.random())

# 读进程执行的任务
def read(q):
    while True:
        value = q.get(True)
        print 'Get value: {0} from queue.'.format(value)

# 测试进程间的通信
def test_communication_between_process():
    q = Queue()
    # 写进程
    pw = Process(target = write,args = (q,))
    # 读进程
    pr = Process(target = read,args = (q,))
    pw.start()
    pr.start()
    pw.join()
    # 因为读任务是死循环，所以要强行结束
    pr.terminate()

def main():
    test_simple_multi_process()
    # 输出：
    '''
    Process will start...
    Run child process 1524, task name is: task2
    Run child process 1728, task name is: task1
    [finished function:do_simple_task in 1.20s]
    [finished function:do_simple_task in 1.20s]
    Process end.
    [finished function:test_simple_multi_process in 1.34s]
    '''

    test_use_process_pool()
    # 输出：
    '''
    Many processes will start...
    Run child process 7568, task name is: task0
    Run child process 7644, task name is: task1
    Run child process 7628, task name is: task2
    Run child process 7620, task name is: task3
    Run child process 7660, task name is: task4
    [finished function:do_simple_task in 1.20s]
    Run child process 7568, task name is: task5
    [finished function:do_simple_task in 1.20s]
    Run child process 7644, task name is: task6
    [finished function:do_simple_task in 1.20s]
    [finished function:do_simple_task in 1.20s]
    [finished function:do_simple_task in 1.20s]
    [finished function:do_simple_task in 1.20s]
    [finished function:do_simple_task in 1.20s]
    All processes end, results is: ['task0', 'task1', 'task2', 'task3', 'task4', 'task5', 'task6']
    [finished function:test_use_process_pool in 2.62s]
    '''

    test_communication_between_process()
    # 输出
    '''
    Put value: A to queue.
    Get value: A from queue.
    Put value: B to queue.
    Get value: B from queue.
    Put value: C to queue.
    Get value: C from queue.
    '''

if __name__ == '__main__':
    main()