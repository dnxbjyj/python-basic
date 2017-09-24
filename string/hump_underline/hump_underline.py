# coding:utf-8
# 聊一聊"驼峰"和"下划线"——Python re.sub()函数详细用法实例讲解
import re

def hump2underline(hunp_str):
    '''
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub

def underline2hump(underline_str):
    '''
    下划线形式字符串转成驼峰形式
    :param underline_str: 下划线形式字符串
    :return: 驼峰形式字符串
    '''
    # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
    sub = re.sub(r'(_\w)',lambda x:x.group(1)[1].upper(),underline_str)
    return sub

def json_hump2underline(hump_json_str):
    '''
    把一个json字符串中的所有字段名都从驼峰形式替换成下划线形式。
    注意点：因为考虑到json可能具有多层嵌套的复杂结构，所以这里直接采用正则文本替换的方式进行处理，而不是采用把json转成字典再进行处理的方式
    :param hump_json_str: 字段名为驼峰形式的json字符串
    :return: 字段名为下划线形式的json字符串
    '''
    # 从json字符串中匹配字段名的正则
    # 注：这里的字段名只考虑英文字母、数字、下划线组成
    attr_ptn = re.compile(r'"\s*(\w+)\s*"\s*:')

    # 使用hump2underline函数作为re.sub函数第二个参数的回调函数
    sub = re.sub(attr_ptn,lambda x : '"' + hump2underline(x.group(1)) + '":',hump_json_str)
    return sub

def test_hump2underline():
    # 供测试用的一些驼峰形式的字符串
    attr1 = 'PersonNamePattern'
    attr2 = 'IPv6Address'
    attr3 = 'personDetailInfo'
    attr4 = 'CCTV'
    attr5 = 'CCTVAddress'
    attr6 = 'name'
    attrs = [attr1,attr2,attr3,attr4,attr5,attr6]

    # 遍历attrs进行匹配和转换，把驼峰形式的字符串转成下划线形式
    for attr in attrs:
        sub = hump2underline(attr)
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

def test_underline2hump():
    attr1 = 'person_name_pattern'
    attr2 = 'ipv6_address'
    attr3 = 'person_detail_info'
    attr4 = 'cctv'
    attr5 = 'cctvaddress'
    attr6 = 'name'
    attrs = [attr1, attr2, attr3, attr4, attr5, attr6]

    for attr in attrs:
        sub = underline2hump(attr)
        print sub

    # 输出：
    '''
    personNamePattern
    ipv6Address
    personDetailInfo
    cctv
    cctvaddress
    name
    '''

def test_json_hump2underline():
    # 待测试json字符串
    json_str = '''
    {
        "englishName":"Tom",
        "age":18,
        "detailInfoTable": {
            "address":"USA",
            "sportsHobby": ["Basketball","Football","Swimming"],
            "contactList":{
                "tel" : "1234567",
                "emailAddress":"tom@test.com"
            }
        },
        "gender":"male"
    }
    '''
    print json_hump2underline(json_str)

    # 输出：
    '''
    {
        "english_name" :"Tom",
        "age" :18,
        "detail_info_table" : {
            "address" :"USA",
            "sports_hobby" : ["Basketball","Football","Swimming"],
            "contact_list" :{
                "tel" : "1234567",
                "email_address" :"tom@test.com"
            }
        },
        "gender" :"male"
    }
    '''

def main():
    # test_hump2underline()
    # test_underline2hump()
    test_json_hump2underline()


if __name__ == '__main__':
    main()