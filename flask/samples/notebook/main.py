# coding:utf-8
# 一个基于Flask和SQLAlchemy+SQLite的极简记事本应用
from __future__ import unicode_literals
from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
import os

# 创建应用程序对象
app = Flask(__name__)
# 获取当前目录的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# sqlite数据库文件存放路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app.sqlite')
# 创建数据库对象
db = SQLAlchemy(app)

class Note(db.Model):
    '''
    记事本数据模型
    '''
    # 主键
    id = db.Column(db.Integer,primary_key = True)
    # 文章标题
    title = db.Column(db.String(80))
    # 文章正文
    body = db.Column(db.Text)
    
    def __init__(self,title,body):
        '''
        初始化方法
        '''
        self.title = title
        self.body = body

@app.route('/')
def home():
    '''
    主页
    '''
    # 渲染首页HTML模板文件
    return render_template('home.html')

@app.route('/notes/create',methods = ['GET', 'POST'])
def create_note():
    '''
    创建笔记
    '''
    if request.method == 'GET':
        # 如果是GET请求，则渲染创建页面
        return render_template('create_note.html')
    else:
        # 从表单请求体中获取请求数据
        title = request.form['title']
        body = request.form['body']
        
        # 创建一个笔记对象
        note = Note(title = title,body = body)
        db.session.add(note)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到笔记列表页面
        return redirect('/notes')

@app.route('/notes',methods = ['GET'])
def list_notes():
    '''
    查询笔记列表
    '''
    notes = Note.query.all()
    # 渲染笔记列表页面目标文件，传入notes参数
    return render_template('list_notes.html',notes = notes)
        
@app.route('/notes/update/<id>',methods = ['GET', 'POST'])
def update_note(id):
    '''
    更新笔记
    '''
    if request.method == 'GET':
        # 根据ID查询笔记详情
        note = Note.query.filter_by(id = id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return render_template('update_note.html',note = note)
    else:
        # 获取最新的笔记标题和正文
        title = request.form['title']
        body = request.form['body']
        
        # 更新笔记
        note = Note.query.filter_by(id = id).update({'title':title,'body':body})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到笔记详情页面
        return redirect('/notes/{id}'.format(id = id))

@app.route('/notes/<id>',methods = ['GET','DELETE'])
def query_note(id):
    '''
    查询笔记详情、删除笔记
    '''
    if request.method == 'GET':
        # 到数据库查询笔记详情
        note = Note.query.filter_by(id = id).first_or_404()
        # 渲染笔记想去页面
        return render_template('query_note.html',note = note)
    else:
        # 删除笔记
        note = Note.query.filter_by(id = id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return '',204
        
if __name__ == '__main__':
    # 以debug模式启动程序
    app.run(debug = True)