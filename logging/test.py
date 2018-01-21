# coding:utf-8
# 测试日志模块logging的用法
import logging

def test_basic_log():
    '''
    测试最基本的打日志
    '''
    logging.debug('test msg1')
    logging.info('test msg2')
    logging.warning('test msg3')

def test_log_with_config():
    logging.basicConfig(level = logging.DEBUG)
    
def main():
    # test_basic_log()
    # 输出：
    '''
    WARNING:root:test msg3
    '''
    # 注：之所以只输出WARNING日志，是因为logging模块默认的日志输出级别是WARNING及以上级别
    # 日志级别关系：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    
    ###
    
    
    
    
if __name__ == '__main__':
    main()