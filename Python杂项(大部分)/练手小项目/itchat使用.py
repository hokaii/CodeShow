"""
TODO
"""
import itchat

#显示及回复消息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    return msg['Text']

"""下载和发送微信附件
@itchat.msg_register(['Picture','Recoding','Attachment','Video'])
def download_files(msg):
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s'%('img' if msg['Type']=='Picture' else 'fil',msg['FileName']),msg['FromUserName'])
    return '%s received'%msg['Type']
"""

itchat.auto_login(hotReload=True)
itchat.run()

#发送消息给文件传输助手
itchat.send('test',toUserName='filehelper')

#获取好友列表,信息内容包括：UserName，City，DisplayName，PYQuanPin，Province，KeyWord，RemarkName，HeadImgUrl
friendslist=itchat.get_friends(update=True)[1:]
print(friendslist)