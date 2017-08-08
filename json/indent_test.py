# coding:utf-8
# 测试缩进
from collections import OrderedDict
import json
import re

def main():
    exception_dict = OrderedDict()
    
    data = OrderedDict()
    data['desc'] = 'this is desc'
    data['cause'] = 'this is cause'
    data['solution'] = 'this is solution'
    
    exception_dict['1001'] = data
    exception_dict['1002'] = data
    exception_dict['1003'] = data
    
    # 读取in.txt
    in_text = ''
    with open('in.txt','r') as fin:
        in_text = fin.read()
    
    # 左边总共需要缩进的空白符
    left_space_pattern = r'^(\s*)"desc"'
    search = re.search(left_space_pattern,in_text,re.M)
    left_space = ''
    if search:
        left_space = search.group(1)
    
    # 左边需要移动的空白符
    move_space_pattern = r'^(\s*)\}\n*\s*\};'
    search = re.search(move_space_pattern,in_text,re.M)
    move_space = ''
    if search:
        move_space = search.group(1)
    
    # 最后一个大括号左边需要移动的字符
    left_move_space_pattern = r'^(\s*)\};'
    search = re.search(left_move_space_pattern,in_text,re.M)
    left_move_space = ''
    if search:
        left_move_space_pattern = search.group(1)
    
    # json项目需要缩进的空白符
    indent_space = ''
    if left_space.count('\t') and move_space.count('\t'):
        indent_space = '\t' * (left_space.count('\t') - move_space.count('\t'))
    elif left_space.count(' ') and move_space.count(' '):
        indent_space = ' ' * (left_space.count(' ') - move_space.count(' '))
    
    # 组装json字符串
    indent = 4
    if indent_space.count('\t') != 0:
        indent = 4 * indent_space.count('\t')
    elif indent_space.count(' ') != 0:
        indent = indent_space.count(' ')
    json_text = json.dumps(exception_dict,indent = indent)
    json_text = json_text.strip().lstrip('{\n').rstrip('}').rstrip()
    
    json_text =  indent_space + '},\n' + json_text
    json_text = re.sub(r'^',left_move_space_pattern,json_text,flags = re.M) + '\n' + left_move_space_pattern + '};'

    # 往in.txt中按照原有缩进格式追加错误码
    replace_pattern = r'^\s*\}\n*\s*\};'
    in_text = re.sub(replace_pattern,json_text,in_text,flags = re.M)
    
    with open('out.txt','w+') as fout:
        fout.write(in_text)
        
if __name__ == '__main__':
    main()