# coding:utf-8
# 封装常用的SSH功能
import paramiko

class SSHUtil(object):
    '''
    封装常用的SSH功能，包括：
    * 远程登录
    * 远程执行命令
    * 上传文件
    * 下载文件
    '''
    def __init__(self,ip,username,password,port = 22):
        '''
        初始化
        
        :param ip: 远程服务器的IP
        :param username: 远程服务器登录用户名
        :param password: 远程服务器登录用户密码
        :param port: 远程服务器的端口，SSH协议默认为22
        '''
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        # 登录，获取SSH对象
        self.login(ip,username,password,port)
    
    def login(self,ip,username,password,port = 22):
        '''
        用paramiko SSH登录远程服务器
        
        :param ip: 远程服务器的IP
        :param username: 远程服务器登录用户名
        :param password: 远程服务器登录用户密码
        :param port: 远程服务器的端口，SSH协议默认为22
        '''
        # 创建一个SSH客户端对象
        self.ssh = paramiko.SSHClient()
        # 设置访问策略
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 与远程主机进行连接
        self.ssh.connect(hostname = ip,port = port,username = username,password = password)

    def execute_command(self,command_str):
        '''
        执行远程命令
        
        :param ssh: SSH连接对象
        :param command_str: 命令字符串
        '''
        input,output,err = self.ssh.exec_command(command_str)
        resp,error = output.read(),err.read()
        if resp:
            return resp
        print 'error occurs: {0}'.format(error)
        raise Exception(error)

    def upload_file(self,local_file_path,remote_file_path):
        '''
        上传文件
        
        :param ssh: SSH连接对象
        :param local_file_path: 本地文件路径
        :param remote_file_path: 远程文件存放路径
        '''
        # 创建sftp对象上传文件
        sftp = self.ssh.open_sftp()
        sftp.put(local_file_path,remote_file_path)
        sftp.close()
        
    def download_file(self,remote_file_path,local_file_path):
        '''
        下载文件
        
        :param ssh: SSH连接对象
        :param remote_file_path: 远程文件路径
        :param local_file_path: 本地文件存放路径
        '''
        # 创建sftp对象下载文件
        sftp = self.ssh.open_sftp()
        sftp.get(remote_file_path,local_file_path)
        sftp.close()

def sample():
    '''
    用法示例
    '''
    # 基本信息
    ip = '192.168.1.xxx'
    username = 'm2fox'
    password = '***'
    
    # 获取SSHUtil对象
    ssh_util = SSHUtil(ip,username,password)
    
    # 执行远程命令
    command = 'ls /home/m2fox'
    print ssh_util.execute_command(command)
    
    # 上传文件
    ssh_util.upload_file('./hello.txt','/home/m2fox/hello.txt')
    
    # 下载文件
    ssh_util.download_file('/home/m2fox/hello.txt','e:/hello.txt')
    print 'end'
    
if __name__ == '__main__':
    sample()