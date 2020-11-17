#! python3
#项目：将带有美国风格日期的文件改名为欧洲风格日期
import shutil, os, re
#Create a regex that matches files with the American date format.创建符合美国风格日期的正则表达式
datePattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""",re.VERBOSE)
#TODO: Loop over the files in the working directory. 循环工作目录中的文件
for amerFilename in os.listdir('.'):
    mo=datePattern.search(amerFilename)
#TODO: Skip files without a date. 没有日期跳过文件
    if mo==None:
        continue
#TODO: Get the different parts if the filename. 获取文件名的不同目录
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
#TODO:From the European-style filename.从欧洲风格的文件名
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
#TODO:Get the full, absolute file paths.得到完整的文件路径
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)
#TODO:Rename the files.重新命名文件
    print('Renaming "%s" to "%s"...'% (amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)   #uncomment after testing