# coding:utf-8
# 把驼峰形式的字符串转成下划线形式
import re

# 供测试用的一些驼峰形式的字符串
attr1 = 'PersonNamePattern'
attr2 = 'IPv6Address'
attr3 = 'personDetailInfo'
attr4 = 'CCTV'
attr5 = 'CCTVAddress'
attr6 = 'name'

attrs = [attr1,attr2,attr3,attr4,attr5,attr6]

# 匹配正则，匹配小写字母和大写字母的分界位置
p = re.compile(r'([a-z]|\d)([A-Z])')

# 遍历attrs进行匹配和转换，把驼峰形式的字符串转成下划线形式
for attr in attrs:
    sub = re.sub(p,r'\1_\2',attr).lower()
    print sub

# 输出：
'''
person_name_pattern
ipv6_address
person_detail_info
cctv
cctvaddress
name
'''