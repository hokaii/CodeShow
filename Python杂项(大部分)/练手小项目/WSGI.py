from wsgiref.simple_server import make_server
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body='<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
#上面的application()函数接受两个参数：
#environ：一个包含所有HTTP的请求信息的dict对象
#start_response：一个发送HTTP相应的函数
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()