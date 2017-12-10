# coding:utf-8
# 测试多进程
import os
import time
from multiprocessing import Process,Pool
from utils import urls,fn_timer
from multiprocessing.pool import MapResult

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

def main():
    # test_simple_multi_process()

    # test_use_process_pool()

if __name__ == '__main__':
    main()