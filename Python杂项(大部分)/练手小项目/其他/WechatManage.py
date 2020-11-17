import itchat
from itchat.content import TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, ATTACHMENT, VIDEO, NOTE, RECORDING
from time import localtime, strftime, time
import re
import os


MSGINFO = {}
FACEPACKAGE = None


def get_friends_info():
    try:
        itchat.auto_login(hotReload=True)
    except:
        itchat.auto_login(hotReload=True, enableCmdQR=True)
    friends_info = itchat.get_friends()
    mps_info = itchat.get_mps()  # 公众号信息
    chartrooms_info = itchat.get_chatrooms()  # 群信息
    head_img_info = itchat.get_head_img()  # 头像信息
    msg_info = itchat.get_msg()
    contact_info = itchat.get_contact()
    for info in chartrooms_info:
        print(info)
    with open('test.jpg', 'wb') as img:
        img.write(head_img_info)
        img.flush()
        img.close()
    with open('wechat_info.txt', 'w', encoding='utf-8') as file:
        for friend in friends_info:
            file.write(str(friend))
            file.write('\n\n\n')


def run():
    try:
        itchat.auto_login(hotReload=True)
    except:
        itchat.auto_login(hotReload=True, enableCmdQR=True)
    itchat.run()


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isGroupChat=True, isMpChat=True)
def save_receive_msg(msg):
    msg_receive_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if 'ActualNickName' in msg:
        msg_from_nickname = msg['ActualNickName']
        msg_from = msg_from_nickname
        msg_from_username = msg['ActualUserName']
        friends = itchat.get_friends(update=True)
        for friend in friends:
            if msg_from_username == friend['UserName']:
                if friend['RemarkName']:
                    msg_from = friend['RemarkName']
                else:
                    msg_from = friend['NickName']
                break
        """
        groups = itchat.get_chatrooms(update=True)
        for group in groups:
            if msg['FromUserName'] == group['UserName']:
                group_name = group['NickName']
                group_menber_count = group['MemberCount']
                break
        if not group_name:
            group_name = '未命名群聊'
        group_name = group_name + '(%s人)' % str(group_menber_count)
        msg_from = group_name + '-->' + msg_from
        """
    else:
        try:
            msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']
            if not msg_from:
                msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
        except:
            msg_from = 'WeChat Official Accounts'
    msg_send_time = msg['CreateTime']
    msg_id = msg['MsgId']
    msg_content = None
    msg_link = None
    # 文本或者好友推荐
    if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
        msg_content = msg['Text']
        print('[Text/Friends]: %s' % msg_content)
    # 附件/视屏/图片/语音
    elif msg['Type'] == 'Attachment' or msg['Type'] == 'Video' or msg['Type'] == 'Picture' or msg['Type'] == 'Recording':
        msg_content = msg['FileName']
        msg['Text'](str(msg_content))
        print('[Attachment/Video/Picture/Recording]: %s' % msg_content)
    # 位置信息
    elif msg['Type'] == 'Map':
        x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度: " + x.__str__() + ", 经度: " + y.__str__()
        else:
            msg_content = r"" + location
        print('[Map]: %s' % msg_content)
    # 分享的音乐/文章
    elif msg['Type'] == 'Sharing':
        msg_content = msg['Text']
        msg_link = msg['Url']
        print('[Sharing]: %s' % msg_content)
    FACEPACKAGE = msg_content
    MSGINFO.update(
        {
            msg_id: {
                "msg_from": msg_from,
                "msg_send_time": msg_send_time,
                "msg_receive_time": msg_receive_time,
                "msg_type": msg['Type'],
                "msg_content": msg_content,
                "msg_link": msg_link
            }
        }
    )
    # updateMsgInfo()


@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def monitor_msg(msg):
    if '撤回了一条信息' in msg['Content']:
        recall_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
        recall_msg = MSGINFO.get(recall_msg_id)
        print('[Recall]: %s' % recall_msg)
        if len(recall_msg_id) < 11:
            itchat.send_file(FACEPACKAGE, toUserName='filehelper')
        else:
            prompt = '+++' + recall_msg.get('msg_from') + '撤回了一条消息+++\n' \
                        '--消息类型: ' + recall_msg.get('msg_type') + '\n' \
                        '--接收时间: ' + recall_msg.get('msg_receive_time') + '\n' \
                        '--消息内容: ' + recall_msg.get('msg_content')
            if recall_msg['msg_type'] == 'Sharing':
                prompt += '\n链接: ' + recall_msg.get('msg_link')
            itchat.send_msg(prompt, toUserName='filehelper')
            if recall_msg['msg_type'] == 'Attachment' or recall_msg['msg_type'] == 'Video' or recall_msg['msg_type'] == 'Picture' or recall_msg['msg_type'] == 'Recording':
                file = '@fil@%s' % (recall_msg['msg_content'])
                itchat.send(msg=file, toUserName='filehelper')
                os.remove(recall_msg['msg_content'])
            MSGINFO.pop(recall_msg_id)


'''更新消息(删除3分钟之前的消息)'''


def update_msg_info():
    need_del_msgs = []
    for msg in MSGINFO:
        msg_time_interval = int(time()) - MSGINFO[msg]['msg_send_time']
        if msg_time_interval > 180:
            need_del_msgs.append(msg)
    if need_del_msgs:
        for msg in need_del_msgs:
            MSGINFO.pop(msg)


if __name__ == '__main__':
    run()
