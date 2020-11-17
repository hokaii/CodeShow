#! python3
#项目：利用webbrowser模块的mapIt.py
import webbrowser, sys
if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()
webbrowser.open('http://map.google.com/maps/place/'+address)