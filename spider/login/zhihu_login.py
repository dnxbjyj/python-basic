# coding:utf-8
# 模拟知乎登录
import sys
import json
import time

import requests
from bs4 import BeautifulSoup as BS

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	# 知乎首页登录URL
	login_url = 'https://www.zhihu.com'
	
	# 获取session，可以持久化保存cookie
	session = requests.Session()
	
	# 从浏览器中获取的headers
	headers = {
	
	}

if __name__ == '__main__':
	main()