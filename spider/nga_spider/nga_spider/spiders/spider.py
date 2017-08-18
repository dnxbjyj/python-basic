# coding:utf-8
import scrapy
from scrapy import Selector
from scrapy import Request

from nga_spider.items import TopicItem,ContentItem

class NgaSpider(scrapy.Spider):
    name = 'NgaSpider'
    host = 'http://bbs.ngacn.cc'
    
    # start_urls是准备爬的初始页面
    start_urls = ['http://bbs.ngacn.cc/thread.php?fid=406']
    
    '''
    # 这个是解析函数，如果不特别指明的话，scrapy抓取回来的页面会由这个函数进行解析。
    # 对页面的处理和分析工作都在此进行，这个示例里我们只是简单地把页面内容打印出来
    def parse(self,resp):
        selector = Selector(resp)
        # 挑选出所有的标题a标签对象列表
        title_list = selector.xpath('//*[@class="topic"]')
        
        # 遍历列表，处理每一个标签
        for title in title_list:
            # 提取出帖子标题内容
            topic = title.xpath('string(.)').extract_first()
            # 提取出帖子的url
            url = self.host + title.xpath('@href').extract_first()
            print topic
            print url
    '''
    # 爬虫的入口，可以做一些初始化的工作，比如从某个文件或数据库中读取起始url
    def start_requests(self):
        for url in self.start_urls:
            # 此处将起始url加入scrapy的待爬取队列，并指定回调解析函数
            # scrapy会自行调度，并访问该url然后把内容拿回来
            yield Request(url = url,callback = self.parse_page)
    
    # 每个标题的解析函数
    def parse_page(self,resp):
        selector = Selector(resp)
        # 挑选出所有的标题a标签对象列表
        title_list = selector.xpath('//*[@class="topic"]')
        
        # 遍历列表，处理每一个标签
        for title in title_list:
            # 提取出帖子标题内容
            topic = title.xpath('string(.)').extract_first()
            # 提取出帖子的url
            url = self.host + title.xpath('@href').extract_first()
            print topic
            print url
            
            # 此处继续把解析出的每个帖子地址加入待爬取队列，并指定解析函数
            yield Request(url = url,callback = self.parse_topic)
            
        # 可以在此处解析翻页信息，从而实现爬取标题列表的多个页面
            
    # 每个帖子的解析函数
    def parse_topic(self,resp):
        selector = Selector(resp)
        
        content_list = selector.xpath('//*[@class="postcontent ubbcode"]')
        for content in content_list:
            content = content.xpath('string(.)').extract_first()
            print content
            item = ContentItem()
            item['url'] = resp.url
            item['content'] = content
            item['author'] = ''
            
            # 这样调用就行了，scrapy会把这个item自动交给我们的DbPipeline取处理
            yield item
            
        # 可以在此处解析翻页信息，从而实现爬取帖子的多个页面