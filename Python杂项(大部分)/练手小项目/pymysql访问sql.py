import pymysql
cxn=pymysql.connect(user='root',password='981129')
#cxn.query('CREAT DATABASE test')
cxn.commit()
cxn.close()