# coding:utf-8
# 对比多线程、多进程和协程下载网页
import requests
import utils
from utils import fn_timer
from multiprocessing.dummy import Pool as thread_pool
from multiprocessing import Pool as process_pool
from gevent.pool import Pool as gevent_pool
from gevent import monkey
# 打动态补丁，把标准库中的thread/socket等替换掉，让它们变成非阻塞的
monkey.patch_all()

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

# 1. 使用线程池下载多个网页的内容
@fn_timer
def download_using_thread_pool(urls):
    pool = thread_pool(100)
    # 第一个参数为函数名，第二个参数一个可迭代对象，为函数所需的参数列表
    resps = pool.map(session.get,urls)
    pool.close()
    pool.join()
    return resps

# 2. 测试使用进程池
@fn_timer
def download_using_process_pool(urls):
    # 创建一个进程池，数字表示一次性同时执行的最大子进程数
    pool = process_pool(100)
    # 任务返回值列表
    results = []
    # 并发执行多个任务，并获取任务返回值
    results = pool.map_async(session.get,urls)
    pool.close()
    pool.join()
    return results.get()

# 3. 使用协程池下载
@fn_timer
def download_using_coroutine_pool(urls):
    # 创建协程池，并设置最大并发量
    pool = gevent_pool(100)
    pool.map(session.get,urls)

def main():
    # 1. 使用线程池下载100个网页
    download_using_thread_pool(utils.urls * 5)
    # 输出：
    '''
    [finished function:download_using_thread_pool in 3.68s]
    '''

    # 2. 使用进程池下载100个网页
    # download_using_process_pool(utils.urls * 5)
    # 输出：
    '''
    卡死了
    '''

    # 3.使用协程池下载20个网页
    download_using_coroutine_pool(utils.urls * 5)
    # 输出：
    '''
    [finished function:download_using_coroutine_pool in 3.46s]
    '''

if __name__ == '__main__':
    main()