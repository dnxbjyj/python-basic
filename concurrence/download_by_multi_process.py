# coding:utf-8
# 使用多进程下载多个网页
import requests
from utils import urls,fn_timer
from multiprocessing import Process,Pool

def download_page(url):
    resp = requests.get(url)
    return resp

# 使用进程池下载多个网页的内容
@fn_timer
def download_using_process_pool(urls):
    # 创建一个进程池，数字表示一次性同时执行的最大子进程数
    pool = Pool(20)
    # 返回值列表
    resps = []
    # 并发执行多个任务，并获取任务返回值
    resps = pool.map_async(requests.get,urls)
    print 'Processes will start...'
    pool.close()
    pool.join()

    print 'All processes end, results is: {0}'.format(resps.get())
    return resps.get()

if __name__ == '__main__':
    resps = download_using_process_pool(urls)
    print len(resps)