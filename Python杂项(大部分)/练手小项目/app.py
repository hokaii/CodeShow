from flask import Flask
from flask import request, Response, json, jsonify
import simplejson
#import json

app=Flask(__name__)

#首页：返回Home

@app.route('/',methods=['GET','POST'])  #装饰器
def home():
    print(request.data)
    receive_data = json.loads(request.form.get('data'))
    lesson = receive_data['code']
    score = receive_data['account']

    info = dict()
    info['name'] = "pengshaugn"
    return jsonify(info)
    #print(receive_data)
    #jsonify(receive_data)
    #return "<h1>hello</h1>"

#登录页：显示登录表单
@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<from action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </from>'''

#处理登录表单，显示登录结果
@app.route('/signin',methods=['POST'])
def signin():
    #需要从request对象读取表单内容：
    if request.method == 'POST':
        print(request.body)
        receive_data = simplejson.loads(request.body)
        print(receive_data)
        jsonify(receive_data)
        return "<h1>hello</h1>"
    """
    if request.form['username']=='zhk' and request.form['password']=='zhk':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password </h3>'"""

if __name__=='__main__':
    app.run()