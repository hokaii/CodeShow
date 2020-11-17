import time
from json import load
from re import findall
from os import system

import AutoTasking
import Email

with open('./ConfigFile/RemoteControl_cmd.json', 'r', encoding='utf-8') as f:
    cmd_dict = load(f)


class RemoteControl:
    def __init__(self, time_interval=5):
        self.email = Email.EmailClass()
        self.msg_num = len(self.email.get('list')['list'][1])
        self.time_interval = time_interval
        self.control_email = '<13059548599@sina.cn>'
    # 运行服务器

    def run(self):
        print('[INFO by RemoteControl]:Start server successfully.')
        while True:
            print("正在运行...")
            self.email.reset_pop()
            mails = self.email.get('list')['list'][1]
            if len(mails) > self.msg_num:
                for i in range(self.msg_num+1, len(mails)+1):
                    res = self.email.get(i)
                    res_from = res[i]['From']
                    res_from = findall(r'<.*?>', res_from)[0].lower()
                    print("[INFO by RemoteControl.]: 接收到来自 " + res_from + " 的邮件")
                    if res_from != self.control_email:
                        continue
                    opera_plat = res[i]['Subject']
                    print("opera_plat:" + opera_plat)
                    command = res[i]['Text']
                    print("command: " + command)
                    if command in cmd_dict:
                        command = cmd_dict[command]
                    print("2cmd" + command)
                    if opera_plat == 'cmd':
                        try:
                            system(command)
                            print('[INFO by RemoteControl]:Run <%s> successfully.' % command)
                        except:
                            print('[ERROR by RemoteControl]: Fail to Run <%s>!' % command)
                    else:
                        auto_tasking = AutoTasking.AutoTasking()
                        self.email.send(attach_path=auto_tasking.screenshot())
                        print('[INFO by RemoteControl]: Send screenshot successfully.')
                self.msg_num = len(mails)+1
            time.sleep(self.time_interval)


if __name__ == '__main__':
    con = RemoteControl()
    con.run()