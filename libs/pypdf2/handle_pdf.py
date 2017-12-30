# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    pdf_handler = MyPDFHandler(u'Eclipse插件开发学习笔记.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./bookmarks-eclipse_plutin.txt',page_offset = 11)
    pdf_handler.save2file(u'Eclipse插件开发学习笔记-目录书签版.pdf')

if __name__ == '__main__':
    main()