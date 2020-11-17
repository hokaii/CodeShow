from base64 import decodebytes
bytes=decodebytes(b'ufnosQ==')

print(str(bytes,'utf-8'))#utf-8可换为gb18030等编码