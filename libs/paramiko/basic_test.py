# coding:utf-8
# 测试paramiko库的基本用法
import paramiko

def login(ip,username,password,port = 22):
    '''
    用paramiko SSH登录远程服务器
    
    :param ip: 远程服务器的IP
    :param username: 远程服务器登录用户名
    :param password: 远程服务器登录用户密码
    :param port: 远程服务器的端口，SSH协议默认为22
    '''
    # 创建一个SSH客户端对象
    ssh = paramiko.SSHClient()
    # 设置访问策略
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 与远程主机进行连接
    ssh.connect(hostname = ip,port = port,username = username,password = password)
    return ssh

def execute_command(ssh,command_str):
    '''
    执行远程命令
    
    :param ssh: SSH连接对象
    :param command_str: 命令字符串
    '''
    input,output,err = ssh.exec_command(command_str)
    resp,error = output.read(),err.read()
    if resp:
        return resp
    print 'error occurs: {0}'.format(error)
    raise Exception(error)

def upload_file(ssh,local_file_path,remote_file_path):
    '''
    上传文件
    
    :param ssh: SSH连接对象
    :param local_file_path: 本地文件路径
    :param remote_file_path: 远程文件存放路径
    '''
    # 创建sftp对象上传文件
    sftp = ssh.open_sftp()
    sftp.put(local_file_path,remote_file_path)
    sftp.close()
    
def download_file(ssh,remote_file_path,local_file_path):
    '''
    下载文件
    
    :param ssh: SSH连接对象
    :param remote_file_path: 远程文件路径
    :param local_file_path: 本地文件存放路径
    '''
    # 创建sftp对象下载文件
    sftp = ssh.open_sftp()
    sftp.get(remote_file_path,local_file_path)
    sftp.close()

def main():
    ip = '192.168.1.xxx'
    username = 'm2fox'
    password = '***'
    
    ssh = login(ip,username,password)
    # print type(ssh)
    
    # command = 'ls /home/m2fox'
    # print execute_command(ssh,command)
    
    upload_file(ssh,'./hello.txt','/home/m2fox/hello.txt')
    download_file(ssh,'/home/m2fox/hello.txt','e:/hello.txt')
    print 'end'
    
if __name__ == '__main__':
    main()