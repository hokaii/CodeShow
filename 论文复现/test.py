
"""
import shutil

f_src = 'C:/Users/hoka/Desktop/test/images/32480432572_56b68358f1_c.jpg'
jpg_list = {'27034876144_4bb43fa46d_c.jpg', '27550317942_be784b24e0_c.jpg'}
for num in jpg_list:
    dst = 'C:/Users/hoka/Desktop/test/images/' + num
    shutil.copyfile(f_src, dst)
print('done!')

f_src = open('./images/32480432572_56b68358f1_c.jpg')
content = f_src.read()
jpg_list = {'27034876144_4bb43fa46d_c.jpg', '27550317942_be784b24e0_c.jpg'}
for num in jpg_list:
    path = './images/' + num
    f_copy = open(path, 'wb')
    f_copy.write(content)
    f_copy.close()
f_src.close()
"""