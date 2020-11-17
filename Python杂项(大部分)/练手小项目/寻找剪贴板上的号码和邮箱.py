#! python3
#寻找剪贴板上的电话号码和邮件地址

import pyperclip,re

phoneRegex=re.compile(r'''(
	(\d{3}|\(\d{3}\))?                    #电话区号 area code
	(\s|-|\.)?                            #分离器 separator
	(\d{3})                               #开始的3位数 first 3 digits
	(\s|-|\.)                             #分离器 separate
	(\d{4})                               #最后的4位数 last 4 digits
	(\s*(ext|x|ext\.)\s*(\d{2,5}))?       #延伸 extension
	)''',re.VERBOSE)

emailRegex=re.compile(r'''(
	[a-zA-Z0-9._%+-]+                     #用户名 username
	@                                     #@ symbol
	[a-zA-Z0-9.-]+                        #域名 domain name
	(\.[a-zA-Z]{2,4})                     #点某物 dot-something
	)''',re.VERBOSE)

text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
	phoneNum='-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x'+groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
