#! python3
#evaluate.py - 项目：评分系统
#根据该系统读取试卷答案及正确答案进行比对得出考试成绩
import os,sys,pyperclip,re
ID=sys.argv[1]
AnswerFile=open('E:\\MyPythonscripts\\answer.txt')
CorectAnswerFile=open('E:\\MyPythonscripts\\项目：生成随机的测验试卷文件\\Geography_answer%s.txt'%ID)
answer=re.compile(r'[ABCD]')
Version=answer.findall(AnswerFile.read())
CorectVersion=answer.findall(CorectAnswerFile.read())
score=0
for i in range(33):
    if Version[i]==CorectVersion[i]:
        score=score+3
AnswerFile.close()
CorectAnswerFile.close()
pyperclip.copy(score)
