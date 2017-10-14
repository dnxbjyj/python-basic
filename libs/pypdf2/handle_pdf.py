# coding:utf-8
# 处理PDF的常用操作
from pdf_utils import MyPDFHandler
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    pdf_handler = MyPDFHandler('./book.pdf')
    pdf_handler.add_bookmarks_by_read_txt('./bookmarks.txt')
    pdf_handler.save2file('./new.pdf')

if __name__ == '__main__':
    main()