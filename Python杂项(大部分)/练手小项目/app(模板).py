#html文件在templates文件夹
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

#首页：返回Home
@app.route('/',methods=['GET','POST'])  #装饰器
def home():
    return render_template('home.html')

#登录页：显示登录表单
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

#处理登录表单，显示登录结果
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    #需要从request对象读取表单内容：
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

if __name__=='__main__':
    app.run()