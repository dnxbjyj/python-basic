# coding:utf-8
# 一个基于Flask和SQLAlchemy+SQLite的极简记事本应用
from __future__ import unicode_literals
from flask import Flask,render_template,redirect,request
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
    return render_template('home.html')

@app.route('/notes/create',methods = ['GET', 'POST'])
def create_note():
    '''
    创建笔记
    '''
    if request.method == 'GET':
        return render_template('create_note.html')
    else:
        title = request.form['title']
        body = request.form['body']
        for i in range(10):
            note = Note(title = '{0}-{1}'.format(i,title),body = body)
            db.session.add(note)
            db.session.commit()
        # 创建完成之后重定向到笔记列表页面
        return redirect('/notes')

@app.route('/notes',methods = ['GET'])
def list_notes():
    '''
    查询笔记列表
    '''
    notes = Note.query.all()
    return render_template('list_notes.html',notes = notes)
    
@app.route('/notes/<id>',methods = ['GET','DELETE'])
def query_note(id):
    '''
    查询笔记详情、删除笔记
    '''
    if request.method == 'GET':
        note = Note.query.filter_by(id = id).first_or_404()
        return render_template('query_note.html',note = note)
    elif request.method == 'DELETE':
        note = Note.query.filter_by(id = id).first_or_404()
        db.session.delete(note)
        db.session.commit()
        return redirect('/notes')
        
if __name__ == '__main__':
    app.run(debug = True)