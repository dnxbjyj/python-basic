# coding:utf-8
# 模拟登录豆瓣
import sys

import requests
from bs4 import BeautifulSoup as BS

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    # 登录URL和首页URL
    login_url = 'https://accounts.douban.com/login'
    index_url = 'https://www.douban.com'
    
    # 会话对象，用于持久化cookie
    session = requests.Session()
    
    # 请求头
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'
    }
    
    
    
if __name__ == '__main__':
    main()
