import poplib
import smtplib
from json import load
from os import path
from email.parser import Parser
from email.header import decode_header, Header
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

import NetworkControl

with open('./ConfigFile/RemoteControl_config.json', 'r') as f:
    options = load(f)


class EmailClass:
    def __init__(self):
        self.info = {}
        if NetworkControl.NetworkControl().is_connected(True):
            self.server = poplib.POP3(options['receiver']['pop3_server'])
            self.server.user(options['receiver']['user_account'])
            self.server.pass_(options['receiver']['password'])
        else:
            pass
    # 接收邮件

    def get(self, *args):
        if NetworkControl.NetworkControl().is_connected(False):
            res = {}
            for arg in args:
                # 邮件数量和占用空间
                if arg == 'stat':
                    res[arg] = self.server.stat()
                # 返回所有邮件的编号
                elif arg == 'list':
                    res[arg] = self.server.list()
                # 获取最新一封邮件
                elif arg == 'latest':
                    mails = self.server.list()[1]
                    response_status, mail_message_lines, octets = self.server.retr(len(mails))
                    msg_content = b'\r\n'.join(mail_message_lines).decode('utf-8')
                    msg = Parser().parsestr(msg_content)
                    result = self.__parse_message(msg)
                    res[arg] = result
                elif type(arg) == int:
                    mails = self.server.list()[1]
                    if arg > len(mails):
                        res[arg] = None
                        continue
                    response_status, mail_message_lines, octets = self.server.retr(arg)
                    msg_content = b'\r\n'.join(mail_message_lines).decode('utf-8')
                    msg = Parser().parsestr(msg_content)
                    result = self.__parse_message(msg)
                    res[arg] = result
                else:
                    res[arg] = None
            return res

    def send(self, content=None, attach_path=None):
        if NetworkControl.NetworkControl().is_connected(False):
            msg = MIMEMultipart()
            # SMTP server
            if not options['sender']['enable_ssl']:
                smtp_server = smtplib.SMTP(options['sender']['smtp_server'], 25)
                smtp_server.set_debuglevel(1)
                smtp_server.login(options['sender']['email_sender'], options['sender']['password'])
            else:
                if options['sender']['port']:
                    try:
                        smtp_server = smtplib.SMTP_SSL(options['sender']['smtp_server'], options['sender']['port'])
                    except:
                        smtp_server = smtplib.SMTP_SSL(options['sender']['smtp_server'])
                else:
                    smtp_server = smtplib.SMTP_SSL(options['sender']['smtp_server'])
                smtp_server.set_debuglevel(1)
                smtp_server.ehlo(options['sender']['smtp_server'])
                smtp_server.login(options['sender']['email_sender'], options['sender']['password'])
            # From
            msg_from = 'Server <%s>' % options['sender']['email_sender']
            from_name, from_addr = parseaddr(msg_from)
            msg['From'] = formataddr((Header(from_name, 'utf-8').encode(), from_addr))
            # To
            msg_to = 'Controller <%s>' % options['sender']['receiver']
            to_name, to_addr = parseaddr(msg_to)
            msg['To'] = formataddr((Header(to_name, 'utf-8').encode(), to_addr))
            # Time
            msg['Date'] = Header(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'utf-8')
            if attach_path is None and content is None:
                return False
            if content is None:
                content = ['Attachment', 'Attachment from your computer']
            msg['Subject'] = Header(content[0])
            msg.attach(MIMEText(content[1], 'plain', 'utf-8'))
            if attach_path:
                with open(attach_path, 'rb') as f:
                    filename = path.basename(attach_path)
                    mime = MIMEBase('attachment', filename.split('.')[-1], filename=filename)
                    mime.add_header('Content-Disposition', 'attachment', filename=filename)
                    mime.add_header('Content-ID', '<0>')
                    mime.add_header('X-Attachment-Id', '0')
                    mime.set_payload(f.read())
                    encoders.encode_base64(mime)
                    msg.attach(mime)
            smtp_server.sendmail(from_addr, [to_addr], msg.as_string())
            smtp_server.quit()
            return True
    # 关闭pop3连接

    def close_pop(self):
        self.server.quit()
    # 重置pop3连接

    def reset_pop(self):
        self.close_pop()
        self.server = poplib.POP3(options['receiver']['pop3_server'])
        self.server.user(options['receiver']['user_account'])
        self.server.pass_(options['receiver']['password'])
    # 解析格式
    # 返回数据格式: {From:, To:, Subject:, Text}

    def __parse_message(self, msg):
        result = {}
        for header in ['From', 'To', 'Subject']:
            result[header] = None
            temp = msg.get(header, '')
            if temp:
                if header == 'Subject':
                    value, charset = decode_header(temp)[0]
                    if charset:
                        value = value.decode(charset)
                    result[header] = value
                else:
                    name, addr = parseaddr(temp)
                    value, charset = decode_header(name)[0]
                    if charset:
                        value = value.decode(charset)
                    result[header] = '%s<%s>' % (value, addr)
        result['Text'] = None
        # 不考虑MIMEMultipart对象:
        if not msg.is_multipart():
            content_type = msg.get_content_type()
            # 只考虑纯文本/HTML内容
            if content_type == 'text/plain' or content_type == 'text/html':
                content = msg.get_payload(decode=True)
                charset = msg.get_charset()
                if charset is None:
                    temp = msg.get('Content-Type', '').lower()
                    pos = temp.find('charset=')
                    if pos >= 0:
                        charset = temp[pos+8:].strip()
                if charset:
                    content = content.decode(charset)
                result['Text'] = content.replace('\r', '').replace('\n', '')
        return result


if __name__ == '__main__':
    email = EmailClass()
    print(email.get(117))
