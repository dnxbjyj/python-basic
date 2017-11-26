# coding:utf-8
# 处理PDF的常用操作
from PyPDF2 import PdfFileReader as reader,PdfFileWriter as writer
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    pdf_handler = MyPDFHandler(u'Greek Mythology.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./bookmarks-GreekMythology.txt',page_offset = 1)
    pdf_handler.save2file(u'Greek Mythology-目录书签版.pdf')

if __name__ == '__main__':
    main()