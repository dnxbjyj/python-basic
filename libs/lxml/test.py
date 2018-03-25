# coding:utf-8
# lxml和BeautifulSoup解析HTML的对比
from bs4 import BeautifulSoup as BS
from collections import OrderedDict
from lxml import etree
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 使用BeautifulSoup
def parse_html_by_BeautifulSoup(html_content):
    '''
    从房价HTML页面中解析出房价数据，返回一个以城市名为key、房价为vlaue的字典
    :param html_content: 房价HTML网页内容
    :return: 以城市名为key、房价为vlaue的字典
    '''
    soup = BS(html_content, 'html.parser')
    tr_list = soup.find('tbody', attrs={'id': 'order_f'}).find_all('tr')
    price_dict = OrderedDict()
    for tr in tr_list:
        city_name = tr.find_all('td')[1].text.strip()
        price_str = tr.find_all('td')[2].text.strip()
        price = int(''.join([d for d in price_str if d != ',']))
        price_dict[city_name] = price
    return price_dict

# 使用lxml
def parse_html_by_lxml(html_content):
    '''
    从房价HTML页面中解析出房价数据，返回一个以城市名为key、房价为vlaue的字典
    :param html_content: 房价HTML网页内容
    :return: 以城市名为key、房价为vlaue的字典
    '''
    html = etree.HTML(html_content)
    cities = html.xpath('//*[@id="order_f"]/tr/td[2]/a/text()')
    cities = [c.strip() for c in cities]
    prices = html.xpath('//*[@id="order_f"]/tr/td[3]/text()')
    prices = [p.strip() for p in prices]
    # 把数字字符串转为整数
    prices = [int(''.join([d for d in price_str if d != ','])) for price_str in prices]
    
    price_tuples = zip(cities,prices)
    price_dict = OrderedDict()
    for price_tuple in price_tuples:
        price_dict[price_tuple[0]] = price_tuple[1]
    return price_dict
    
def main():
    with open('./data.txt','r') as fin:
        # 用unicode编码读取文本文件
        html_content = unicode(fin.read(),'utf-8')
        
    print json.dumps(parse_html_by_BeautifulSoup(html_content)).decode('unicode-escape').encode('gbk')
    print json.dumps(parse_html_by_lxml(html_content)).decode('unicode-escape').encode('gbk')

if __name__ == '__main__':
    main()