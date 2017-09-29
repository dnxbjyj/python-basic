# coding:utf-8
from gittle import Gittle
import os

def get_direct_sub_dirs(path):
    '''
    获取一个目录下的所有直接子目录的路径列表
    :param path: 父目录
    :return: 直接子目录列表
    '''
    walk = os.walk(path)
    sub_dirs = []
    for d in walk:
        if d[0] in [path]:
            for sub_dir in d[1]:
                sub_dirs.append(os.path.join(d[0],sub_dir))
    return sub_dirs

def is_git_repo(path):
    '''
    判断一个路径是不是git仓库
    :param path: 要判断的路径
    :return: 是否是git路径
    '''
    try:
        repo = Gittle(path)
        return True
    except Exception, e:
        return False

def push_git_repo(path):
    '''
    把git路径的内容推到远程
    :param path: git仓库根目录
    :return: None
    '''
    os.chdir(path)

    add_command = 'git add -A'
    os.popen(add_command)
    print 'finished git add in repo: {repo_path}'.format(repo_path = os.path.basename(path))

    commit_command = 'git commit -m "{msg}"'.format(msg='add some code.')
    os.popen(commit_command)
    print 'finished git commit in repo: {repo_path}'.format(repo_path= os.path.basename(path))

    push_command = 'git push origin master'
    os.popen(push_command)
    print 'finished git push in repo: {repo_path}\n'.format(repo_path= os.path.basename(path))

def batch_push_git_repo(parent_path):
    '''
    搜索一个父目录下的所有直接子目录，把是git仓库的目录的内容推送到远程
    :param parent_path: 父目录
    :return: None
    '''
    dirs = get_direct_sub_dirs(parent_path)
    for d in dirs:
        if is_git_repo(d):
            push_git_repo(d)

def main():
    git_root1 = 'e:/code'
    git_root2 = 'e:/code/android'
    batch_push_git_repo(git_root1)

if __name__ == '__main__':
    main()