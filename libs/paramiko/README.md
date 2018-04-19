# paramiko库基本用法——建立SSH连接、远程执行命令和上传下载文件

> 本文讲述的核心库：`paramiko`
> 官方文档：http://docs.paramiko.org/en/2.4/

# 准备工作：paramiko库安装、测试环境搭建
### paramiko库安装
`pip install paramiko`

### 测试环境搭建
测试和远程服务器的交互，那首先得有一台远程主机，可以在阿里云申请虚拟机，但是成本有点高。如果想要便捷一点，其实可以在自己电脑上用Vmware搭建一个Linux虚拟机充当远程主机，搭建方法可以参考：[VMware Workstation + Lubuntu打造极速虚拟机环境](https://www.jianshu.com/p/52314cda60b9)

# 建立和远程服务器的SSH连接
在远程服务器上执行各种操作的前提是首先建立和远程服务器的连接，这里使用SSH连接：
```python
# coding:utf-8
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

def main():
    ip = '192.168.xxx.xxx'
    username = '***'
    password = '***'
    ssh = login(ip,username,password)
    print type(ssh)
    
if __name__ == '__main__':
    main()
```
执行上述代码，输出：
```
<class 'paramiko.SSHClient'>
```
可见，当和远程服务器建立的SSH连接成功后，会创建出一个SSHClient对象。

# 在远程服务器上执行命令
```python
# coding:utf-8
import paramiko

def execute_command(ssh,command_str):
    '''
    执行远程命令
    
    :param ssh: SSH连接对象
    :param command_str: 命令字符串
    '''
    input,output,err = ssh.exec_command(command_str)
    resp,error = output.read(),err.read()
    # 这里对命令执行结果和异常的处理方式还有待思考
    if resp:
        return resp
    print 'error occurs: {0}'.format(error)
    raise Exception(error)

def main():
    ip = '192.168.xxx.xxx'
    username = '***'
    password = '***'
    ssh = login(ip,username,password)
    
    command = 'ls /home/m2fox'
    print execute_command(ssh,command)
    
if __name__ == '__main__':
    main()
```
执行上面代码，输出：
```
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
tmp
Videos
```
这是在我的虚拟机上`/home/m2fox`目录下的文件和文件夹列表。

# 上传、下载文件
* 首先在当前目录创建一个`hello.txt`文件，其文件内容如下：
```
hello, paramiko!
```

* 上传、下载代码：
```python
# coding:utf-8
import paramiko

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
    ip = '192.168.xxx.xxx'
    username = '***'
    password = '***'
    ssh = login(ip,username,password)
    
    # 上传文件
    upload_file(ssh,'./hello.txt','/home/m2fox/hello.txt')
    # 下载文件
    download_file(ssh,'/home/m2fox/hello.txt','e:/hello.txt')
    
if __name__ == '__main__':
    main()
```
执行上述代码，然后到虚拟机的`/home/m2fox/`目录查看：
![](https://upload-images.jianshu.io/upload_images/8819542-c8adfe2f1f0b2d87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

发现`hello.txt`文件以已经被成功上传到`/home/m2fox/`目录，文件内容也是正确的。

再打开本地E盘根目录，发现从虚拟机下载`hello.txt`成功：
![](https://upload-images.jianshu.io/upload_images/8819542-8c5f70c30617e149.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# SSHUtil封装
将上面讲到的几项基本功能封装成一个类：`SSHUtil`，便于以后使用。
```python
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
    ip = '192.168.xxx.xxx'
    username = '***'
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
```

# 总结
本文讲了paramiko库提供的几项基本功能的用法：建立SSH连接、执行远程命令和上传、下载文件。其实paramiko库还有更多丰富的功能，可以去官方文档进行了解，也可以基于`执行远程命令`这个基础能力，结合Shell命令、脚本，开发出自己需要的更为丰富的功能，比如批量上传文件、重启远程进程、读取远程配置文件等等，最重要的是**学以致用**。

---
获取本文源代码：[我的GitHub](https://github.com/dnxbjyj/python-basic/tree/master/libs/paramiko)