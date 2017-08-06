# coding:utf-8
# 中文正则匹配测试
import sys
import re

from docx import Document

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    document = Document('e:/docs/demo3.docx')
    
    # 从每个段落文字中匹配出联系方式
    paragraphs = document.paragraphs
    for para in paragraphs:
        text = para.text
        print text
        contact_pattern = re.compile(u'联系方式：(.+)$')
        print re.findall(contact_pattern,text)
        print '-----------------'
        
    
if __name__ == '__main__':
    main()