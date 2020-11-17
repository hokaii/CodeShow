#! python3
#pw.py - 项目：口令保管箱
#使用该口令管理器软件，利用一个主控口令，解锁口令管理器。然后将某个账户口令拷贝到剪贴板，再将它粘贴到网站的口令输入框。

PASSWORDS={'email':'ASDFskf3j23i34jfssldfSDfsdf',
	   'blog':'Vsndfjsdf343SDF#$F3f34fsf34h',
	   'luggage':'1234534'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account=sys.argv[1]    #  first command line arg is the account name   第一条命令行ARG是帐户名

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' +account+' copied to clipboard.')
else:
	print('There is no account named ' + account)

r=input()
