#！python3
# -*- coding:utf-8 -*-
#生成30份地理试卷和30份答案
import random
Data_base={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','黑龙江':'哈尔滨','吉林':'长春','辽宁':'沈阳','内蒙古':'呼和浩特','河北':'石家庄','新疆':'乌鲁木齐','甘肃':'兰州','青海':'西宁','陕西':'西安','宁夏':'银川','河南':'郑州','山东':'济南','山西':'太原','安徽':'合肥','湖北':'武汉','湖南':'长沙','江苏':'南京','四川':'成都','贵州':'贵阳','云南':'昆明','广西':'南宁','西藏':'拉萨','浙江':'杭州','江西':'南昌','广东':'广州','福建':'福州','台湾':'台北','海南':'海口','香港':'香港','澳门':'澳门'}
for quizNum in range(30):
    quizFile=open('Geography%s.txt'%(quizNum+1),'w')
    answerFile=open('Geography_answer%s.txt'%(quizNum+1),'w')
    quizFile.write('姓名:__________ 班级:__________ 分数:__________')
    quizFile.write((' '*20)+'Geography Quiz (from NO.%s)'%(quizNum+1))
    quizFile.write('\n\n')
    quizFile.write('一、选择题，请选择各个省份的首府（满分100）\n')
    geography=list(Data_base.keys())
    capital=list(Data_base.values())
    random.shuffle(geography)
    for questionNum in range(34):
        correctAnswer=Data_base[geography[questionNum]]
        wrongAnswers=list(Data_base.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s、%s的首府是:(  )\n'%(questionNum+1,geography[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')
        answerFile.write('%s. %s\n'%(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()