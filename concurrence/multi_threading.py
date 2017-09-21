# coding:utf-8
# 测试多线程
import threading
import time
from utils import fn_timer
from multiprocessing.dummy import Pool
import requests
from utils import urls

# 耗时任务：听音乐
def music(name):
    print 'I am listening to music {0}'.format(name)
    time.sleep(1)

# 耗时任务：看电影
def movie(name):
    print 'I am watching movie {0}'.format(name)
    time.sleep(5)

# 单线程操作：顺序执行听10首音乐，看2部电影
@fn_timer
def single_thread():
    for i in range(10):
        music(i)
    for i in range(2):
        movie(i)

# 多线程执行：听10首音乐，看2部电影
@fn_timer
def multi_thread():
    # 线程列表
    threads = []
    for i in range(10):
        # 创建一个线程，target参数为任务处理函数，args为任务处理函数所需的参数元组
        threads.append(threading.Thread(target = music,args = (i,)))
    for i in range(2):
        threads.append(threading.Thread(target = movie,args = (i,)))

    for t in threads:
        # 设为守护线程
        t.setDaemon(True)
        # 开始线程
        t.start()
    for t in threads:
        t.join()

# 使用线程池执行：听10首音乐，看2部电影
@fn_timer
def use_pool():
    # 设置线程池大小为20，如果不设置，默认值是CPU核心数
    pool = Pool(20)
    pool.map(movie,range(2))
    pool.map(music,range(10))
    pool.close()
    pool.join()

# 应用：使用单线程下载多个网页的内容
@fn_timer
def download_using_single_thread(urls):
    resps = []
    for url in urls:
        resp = requests.get(url)
        resps.append(resp)
    return resps

# 应用：使用多线程下载多个网页的内容
@fn_timer
def download_using_multi_thread(urls):
    threads = []
    for url in urls:
        threads.append(threading.Thread(target = requests.get,args = (url,)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

# 应用：使用线程池下载多个网页的内容
@fn_timer
def download_using_pool(urls):
    pool = Pool(20)
    # 第一个参数为函数名，第二个参数一个可迭代对象，为函数所需的参数列表
    resps = pool.map(requests.get,urls)
    pool.close()
    pool.join()
    return resps

def main():
    # 测试单线程
    # single_thread()
    # 输出：
    '''
    I am listening to music 0
    I am listening to music 1
    I am listening to music 2
    I am listening to music 3
    I am listening to music 4
    I am listening to music 5
    I am listening to music 6
    I am listening to music 7
    I am listening to music 8
    I am listening to music 9
    I am watching movie 0
    I am watching movie 1
    [finished function:single_thread in 20.14s]
    '''

    # 测试多线程
    # multi_thread()
    # 输出：
    '''
    I am listening to music 0
    I am listening to music 1
    I am listening to music 2
    I am listening to music 3
    I am listening to music 4
    I am listening to music 5
    I am listening to music 6
    I am listening to music 7
    I am listening to music 8
    I am listening to music 9
    I am watching movie 0
    I am watching movie 1
    [finished function:multi_thread in 5.02s]
    '''

    # 测试线程池
    # use_pool()
    # 输出：
    '''
    I am listening to music 0
    I am listening to music 1
    I am listening to music 2
    I am listening to music 3
    I am listening to music 4
    I am listening to music 5
    I am listening to music 6
    I am listening to music 7
    I am listening to music 8
    I am listening to music 9
    I am watching movie 0
    I am watching movie 1
    [finished function:use_pool in 6.12s]
    '''

    # 1.使用单线程
    # resps = download_using_single_thread(urls)
    # print len(resps)
    # 输出：
    '''
    [finished function:download_using_single_thread in 6.18s]
    20
    '''
    # 2. 使用多线程
    # download_using_multi_thread(urls)
    # 输出：
    '''
    [finished function:download_using_multi_thread in 0.73s]
    '''

    # 3.使用线程池
    # resps = download_using_pool(urls)
    # print len(resps)
    # 输出：
    '''
    [finished function:download_using_pool in 0.84s]
    20
    '''

if __name__ == '__main__':
    main()
