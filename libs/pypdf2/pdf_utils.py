# coding:utf-8
# 封装的PDF文档处理工具
'''
pypdf2 doc: http://pythonhosted.org/PyPDF2/
'''
from PyPDF2 import PdfFileReader as reader,PdfFileWriter as writer
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MyPDFHandler(object):
    '''
    封装的PDF文件处理类
    '''
    def __init__(self,pdf_file_path):
        '''
        用一个PDF文件初始化
        :param pdf_file_path: PDF文件路径
        '''
        # 只读的PDF对象
        self.__pdf = reader(pdf_file_path)

        # 获取PDF文件名（不带路径）
        self.__file_name = os.path.basename(pdf_file_path)

        self.__writeable_pdf = writer()
        # 可写的PDF对象
        self.__writeable_pdf.cloneDocumentFromReader(self.__pdf)

    def get_pages_num(self):
        '''
        获取PDF文件的页数
        :return: 页数
        '''
        return self.__pdf.getNumPages()

    def get_file_name(self):
        '''
        获取PDF文件名（不带路径）
        :return: PDF文件名
        '''
        return self.__file_name

    def save2file(self,new_file_name):
        '''
        将修改后的PDF保存成文件
        :param new_file_name: 新文件名，不要和原文件名相同
        :return: None
        '''
        # 保存修改后的PDF文件内容到文件中
        with open(new_file_name, 'wb') as fout:
            self.__writeable_pdf.write(fout)
        print 'save2file success! new file name is: {0}'.format(new_file_name)

    def add_one_bookmark(self,title,page,parent = None, color = None,fit = '/Fit'):
        '''
        往PDF文件中添加单条书签，并且保存为一个新的PDF文件
        :param str title: 书签标题
        :param int page: 书签跳转到的页码，为1表示第一页
        :paran parent: A reference to a parent bookmark to create nested bookmarks.
        :param tuple color: Color of the bookmark as a red, green, blue tuple from 0.0 to 1.0
        :param list bookmarks: 是一个'(书签标题，页码)'二元组列表，举例：[(u'tag1',1),(u'tag2',5)]，页码为1代表第一页
        :param str fit: 跳转到书签页后的缩放方式
        :return: None
        '''
        # 为了防止乱码，这里对title进行utf-8编码
        self.__writeable_pdf.addBookmark(title.decode('utf-8'),page - 1,parent = parent,color = color,fit = fit)
        print 'add_one_bookmark success! bookmark title is: {0}'.format(title)

    def add_bookmarks(self,bookmarks):
        '''
        批量添加书签
        '''
        for title,page in bookmarks:
            self.add_one_bookmark(title,page)
        print 'add_bookmarks success! add {0} pieces of bookmarks to PDF file'.format(len(bookmarks))

    def read_bookmarks_from_txt(self,txt_file_path):
        '''
        从文本文件中读取书签列表
        文本文件有若干行，每行一个书签，内容格式为：
        书签标题 页码
        注：中间用空格隔开，页码为1表示第1页
        :param txt_file_path: 书签信息文本文件路径
        :return: 书签列表
        '''
        bookmarks = []
        with open(txt_file_path,'r') as fin:
            for line in fin:
                line = line.strip()
                if not line:
                    continue
                title = line.split()[0].strip()
                page = int(line.split()[1].strip())
                bookmarks.append((title,page))
        return bookmarks

    def add_bookmarks_by_read_txt(self,txt_file_path):
        '''
        通过读取书签列表信息文本文件，将书签批量添加到PDF文件中
        :param txt_file_path: 书签列表信息文本文件
        :return: None
        '''
        bookmarks = self.read_bookmarks_from_txt('bookmarks.txt')
        self.add_bookmarks(bookmarks)
        print 'add_bookmarks_by_read_txt success!'
