# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    pdf_handler = MyPDFHandler(u'高等数学 第7版 上册 同济大学.pdf',mode = mode.NEWLY)
    pdf_handler.add_bookmarks_by_read_txt('./bookmarks.txt',page_offset = 15)
    pdf_handler.save2file(u'高等数学 第7版 上册 同济大学-目录书签版.pdf')

if __name__ == '__main__':
    main()