#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = '13059548599@163.com'
password = 'hoka506'
pop3_server = 'pop.163.com'

# 文本邮件的内容也是str,还需要检测编码, 否则非utf8编码的邮件无法显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos > 0:
            charset = content_type[pos+8:].strip()
    return charset

def decode_str(s):
    # decode_header()返回一个list,因为像Cc,Bcc,这样的字段可能包含多个邮件地址,所以解析出的会有多个元素
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# index用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                # 解码subject
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    # parseaddr 用来解析邮件地址,结果为一个列表,第一项是user,第二项是地址
                    hdr, addr, = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    # 这里判断是否multipart,是的话,里面的数据是无用的
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' '*indent, n))
            print('%s---------------------' % (' ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset=guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print('%sText: %s' % (' '*indent, content + '...'))
            else:
                print('%sAttachment: %s' % (' ' * indent, content_type))

if __name__ == '__main__':
    server = poplib.POP3(pop3_server)
    server.user(email)
    server.pass_(password)

    print('Message: %s. Size: %s' % server.stat())
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 20073,...]
    #print(mails)

    index = len(mails)
    resp, lines, octets = server. retr(index)

    # lines存储了邮件的原始文本的每一行,可获得整个邮件的原始文本
    msg_content = b'\r\n'.join(lines) . decode('utf-8')
    # 将邮件内容解析为 Messag 对象
    msg = Parser().parsestr(msg_content)
    print_info(msg)

    # 可以根据邮件索引号直接从服务器删除邮件
    # server.dele(index)
    server.quit()