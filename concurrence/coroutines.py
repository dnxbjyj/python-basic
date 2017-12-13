# coding:utf-8
# 测试协程
import requests
import gevent
import utils
from utils import fn_timer
from gevent.pool import Pool
from gevent import monkey
# 打动态补丁，把标准库中的thread/socket等替换掉，让它们变成非阻塞的
monkey.patch_all()

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

@fn_timer
def download_using_single_thread(urls):
    '''
    顺序执行下载多个网页
    :param urls: 要下载的网页内容
    :return: 响应列表
    '''
    resps = []
    for url in urls:
        resps.append(session.get(url))
    return resps

@fn_timer
def download_using_coroutine(urls):
    '''
    使用协程下载
    :param urls: 要下载的网页内容
    :return: 响应列表
    '''
    spawns = []
    for url in urls:
        spawns.append(gevent.spawn(session.get,url))
    # 在遇到IO操作时，gevent会自动切换，并发执行（异步IO）
    gevent.joinall(spawns)

@fn_timer
def download_using_coroutine_pool(urls):
    # 创建协程池，并设置最大并发量
    pool = Pool(20)
    pool.map(session.get,urls)

def main():
    # 1.使用单线程下载20个网页
    download_using_single_thread(utils.urls)
    # 输出：
    '''
    [finished function:download_using_single_thread in 1.83s]
    '''

    # 2.使用协程下载20个网页
    download_using_coroutine(utils.urls)
    # 输出：
    '''
    [finished function:download_using_coroutine in 0.69s]
    '''

    # 3.使用协程池下载20个网页
    download_using_coroutine_pool(utils.urls)
    # 输出：
    '''
    [finished function:download_using_coroutine_pool in 0.78s]
    '''

if __name__ == '__main__':
    main()