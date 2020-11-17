import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个socket
s.connect(('www.sina.com.cn',80)) #建立连接
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer=[]
while True:         #接收数据
    d=s.recv(1024)        #每次最多接收1k字节
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()             #关闭连接
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))        #使用utf-8码标准转码
with open('sina.html','wb')as f:     #把接收的数据写入到文件中
    f.write(html)