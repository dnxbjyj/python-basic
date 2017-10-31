# coding:utf-8
# 校验一个python文件的合法性
import sys
import os
import json

def main():
    current_file_path = sys.argv[1]
    # 判断文件是否存在
    if not os.path.exists(current_file_path):
        print 'validate error! the file is not exist!'
        os.system('pause')

    # 判断文件是否是json文件
    if os.path.basename(current_file_path).split('.')[-1] != 'json':
        print 'validate error! the file is not a json file!'
        os.system('pause')

    print 'start to validate the json file: {0}'.format(os.path.basename(current_file_path))
    with open(current_file_path,'r') as fin:
        try:
            content = json.load(fin)
        except ValueError,e:
            print 'validate error! invalid json file: {0}'.format(e.message)
            os.system('pause')
        finally:
            print 'validate OK! it is a valid json file.'
            os.system('pause')

if __name__ == '__main__':
    main()