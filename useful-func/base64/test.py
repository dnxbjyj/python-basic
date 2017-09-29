# coding:utf-8
# 测试base64编解码
import base64

def main():
    s = '123abc'

    # 编码
    print base64.b64encode(s)
    # 输出：MTIzYWJj

    # 解码
    print base64.b64decode('MTIzYWJj')
    # 输出：123abc

if __name__ == '__main__':
    main()