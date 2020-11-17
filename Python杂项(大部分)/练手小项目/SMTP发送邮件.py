#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = '13059548599@sina.cn'
receiver = '13059548599@163.com'
subject = 'mailcontrol'
smtpserver = 'smtp.163.com'
username = '13059548599@sina.cn'
password = 'zhk7539510.'

#如果要发送HTML，则如下
#msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>','html','utf-8')
msg = MIMEText('changemywall please and i am hoka','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'hoka<13059548599@sina.cn>'  
msg['To'] = "13059548599@163.com"
smtp = smtplib.SMTP()
smtp.connect('smtp.sina.cn')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


"""
#发送附件
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

sender = '13059548599@sina.cn'
receiver = '13059548599@163.com'
subject = 'mailcontrol'
smtpserver = 'smtp.163.com'
username = '13059548599@sina.cn'
password = 'zhk7539510.'

# 如果要发送HTML，则如下
# msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>','html','utf-8')
msg=MIMEMultipart()
msg.attach(MIMEText('changemywall please and i am hoka', 'plain', 'utf-8'))  # 中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'hoka<13059548599@sina.cn>'
msg['To'] = "13059548599@163.com"

with open('H:\\Python\\LiAng\\Scripts\\screenshots\\2018Oct24_2246.png','rb') as f:
    mime=MIMEBase('image','png',filename='2018Oct24_2246.png')
    mime.add_header('Content-Disposition','attachment',filename='2018Oct24_2246.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

smtp = smtplib.SMTP()
smtp.connect('smtp.sina.cn')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
"""