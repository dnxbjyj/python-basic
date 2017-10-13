# coding:utf-8
# 往pdf文件中添加书签
'''
pypdf2 doc: http://pythonhosted.org/PyPDF2/
'''
from PyPDF2 import PdfFileReader as reader,PdfFileWriter as writer

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # 读取PDF文件，创建PdfFileReader对象
    book = None
    with open('./book.pdf','rb') as fin:
        book = reader('./book.pdf')

    # 创建PdfFileWriter对象，并用拷贝reader对象进行初始化
    pdf = writer()
    pdf.cloneDocumentFromReader(book)

    # 添加书签
    # 注意：页数是从0开始的，中文要用unicode字符串，否则会出现乱码
    pdf.addBookmark(u'第0页abc123',0)

    # 保存修改后的PDF文件内容到文件中
    with open('./out.pdf','wb') as fout:
        pdf.write(fout)

if __name__ == '__main__':
    main()