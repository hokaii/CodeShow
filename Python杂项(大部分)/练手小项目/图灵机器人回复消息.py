import requests
import itchat
#向图灵机器人发送消息，得到图灵机器人的回复消息
def get_response(msg):
    apiUrl='http://www.tuling123.com/openapi/api'
    apiKey='f1b6d7cb959c419a87fdd5c68be55bba'
    data={
    'key':apiKey,
    'info':msg,
    'userid':'pth-robot',
    }
    try:
        r=requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return
#注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    #为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复a
    defaultReply='I received: '+msg['Text']
    #如果图灵Key出现问题，那么reply将会是None
    reply=get_response(msg['Text'])
    #a or b的意思是，如果a有内容，那么返回a，否则返回b
    return reply or defaultReply
itchat.auto_login(hotReload=True)
itchat.run()