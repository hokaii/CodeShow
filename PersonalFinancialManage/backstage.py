#-*- coding:utf-8 -*-
import datetime
import pymysql
import threading

MYSQL_HOST = '47.97.183.25'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_PORT = 3306
DATABASE = 'financemanage'
CHARSET = 'utf-8'
lock = threading.Lock()


# 后台类,实际包含DAO层
class Backstage:
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=DATABASE, charset=CHARSET):
        try:
            self.db = pymysql.Connection(host=host, user=username, password=password,
                                         database=database, port=port)
            # 使返回的为字典
            self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(e.args)
        self.id = 0

    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = "insert into %s (%s) values (%s)" % (table, keys, values)
        #print("sql", sql)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            return True
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
            return False

    def insert_many(self, table, data):
        if isinstance(data, list) or isinstance(data, tuple):
            keys = str(tuple(data[0].keys())).replace('(', '').replace(')', '').replace("'", '')
            sql = "insert into %s (%s) value' % (table, keys) + ' (' + '%s, ' * (len(data[0].keys()) - 1) + '%s);"
            values = [tuple(d.values()) for d in data]
            print("keys", keys)
            print("sql", sql)
            print("values", values)

            if lock.acquire():
                try:
                    self.cursor.executemany(sql, values)
                    self.db.commit()
                    return True
                except pymysql.MySQLError as e:
                    print(e.args)
                    self.db.rollback()
                    return False
                finally:
                    lock.release()
        return False

    def find_key_val(self, table, key_val):
        sql = None
        if isinstance(key_val, str):
            sql = "SELECT * FROM `%s` WHERE %s ;" % (table, key_val)
            print("sql", sql)
        elif isinstance(key_val, dict):
            sql_where = ''
            for item in key_val.items():
                row_str = str(item[0]) + '=' + str(item[1]) + ' and '
                sql_where += row_str
            sql_where = sql_where[:-4]
            sql = "SELECT * FROM `%s` WHERE %s ;" % (table, sql_where)
        if sql:
            try:
                self.cursor.execute(sql)
                data = self.cursor.fetchall()
                if len(data) > 0:
                    return data
                return None
            except pymysql.MySQLError as e:
                print(e.args)
        return None

    def find_by_sql(self, sql):
        if sql:
            try:
                self.cursor.execute(sql)
                data = self.cursor.fetchall()
                if len(data) > 0:
                    return data
                return None
            except pymysql.MySQLError as e:
                print(e.args)
        return None

    def del_by_sql(self, sql):
        if sql:
            try:
                self.cursor.execute(sql)
                self.db.commit()
                return True
            except pymysql.MySQLError as e:
                print(e.args)
                self.db.rollback()
        return None

    def update_by_sql(self, sql):
        print("sql", sql)
        if sql:
            try:
                self.cursor.execute(sql)
                self.db.commit()
                return True
            except pymysql.MySQLError as e:
                print(e.args)
                self.db.rollback()
        return None

    def close(self):
        try:
            self.cursor.close()
        except:
            pass
        try:
            self.db.close()
        except:
            pass

    def verify(self, account, code):
        results = self.find_key_val("user", "user_id='%s'"%account)
        print(results[0]['password'])
        if results[0]['password'] == code:
            return True
        else:
            return False

    def insert_register(self, insert_dict):
        if self.insert("user", insert_dict):
            return True
        else:
            return False

    def insert_bill(self, insert_dict, flag=True):
        if flag:
            if self.insert("income", insert_dict):
                return True
            else:
                return False
        else:
            if self.insert("pay", insert_dict):
                return True
            else:
                return False

    def select_user_name(self, user_id):
        results_list = []
        results_list.append(self.find_key_val("user", "user_id=%s"%user_id))
        return results_list

    def select_all_info(self, user_id):
        results_list = []
        results_list.append(self.find_key_val("income", "user_id="+user_id))
        results_list.append(self.find_key_val("pay", "user_id=" + user_id))
        #results_list.append(self.find_key_val("login_record", "user_id=" + user_id))
        #results_list.append(self.find_key_val("op_record", "user_id=" + user_id))
        for result in results_list:
            print(result)
        return results_list

    def select_time(self, start_time, end_time, user_id):
        results_list = []
        results_list.append(self.find_key_val("income", "user_id="+user_id + " and income_time between " + repr(start_time) +
                                              " and " + repr(end_time)))
        results_list.append(self.find_key_val("pay", "user_id="+user_id + " and pay_time between " + repr(start_time) +
                                              " and " + repr(end_time)))
        for result in results_list:
            print(result)
        return results_list

    def select_type(self, type, user_id):
        results_list = []
        if type == "全部":
            return self.select_all_info(user_id)
        results_list.append(
            self.find_key_val("income", "user_id=" + user_id + " and income_type= " + repr(type)))
        results_list.append(
            self.find_key_val("pay", "user_id=" + user_id + " and pay_type= " + repr(type)))
        for result in results_list:
            print("result", result)
        return results_list

    def select_keyword(self, keyword, user_id):
        keyword = "%" + keyword + "%"
        print(keyword)
        results_list = []
        results_list.append(
            self.find_key_val("income", "user_id= %s and income_type like %s or income_name like %s or income_remark like %s"%
                              (user_id, repr(keyword),repr(keyword), repr(keyword))))
        results_list.append(
            self.find_key_val("pay",
                              "user_id= %s and pay_type like %s or pay_name like %s or pay_remark like %s" %
                              (user_id, repr(keyword), repr(keyword), repr(keyword))))
        for result in results_list:
            print("result", result)
        return results_list

    def select_max_id(self, table, id):
        results = self.find_by_sql("select %s from %s order by %s desc"%(id, table, id))
        if results[0]:
            return results[0][id]
        return 1

    def del_data(self, id, flag=True):
        if flag:
            if self.del_by_sql("delete from income where income_id = %s"%(id)):
                return True
            else:
                return False
        else:
            if self.del_by_sql("delete from pay where pay_id = %s"%(id)):
                return True
            else:
                return False

    def update_data(self, phone_num, email, password, id):
        if self.update_by_sql("update `user` set phone_number=%s where user_id=%s"%(phone_num, id)) and self.update_by_sql("update `user` set email=%s where user_id=%s"%(email, id)) and self.update_by_sql("update `user` set password=%s where user_id=%s"%(password, id)):
            return True
        else:
            return False

    def update_table_data(self, id, key, value, flag=True):
        print("id", id, "key", key, "value", value)
        if flag:
            if self.update_by_sql("update income set %s = %s where income_id = %s"%(key, value, id)):
                return True
            else:
                return False
        else:
            if self.update_by_sql("update pay set %s = %s where pay_id = %s"%(key, value, id)):
                pass


# 测试
if __name__ == '__main__':
    backstage = Backstage()
    print(backstage.verify("user", "123"))
    #backstage.insert_register({"user_id": "5", "phone_number": "", "email": "", "register_time": datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"), "password": "123"})
    #result = backstage.find_key_val("user", "password")
    #print(result)
    #backstage.select_all_info(repr("张三"))
    #backstage.select_type("理财", repr("1"))
    #backstage.select_keyword("余额宝", repr("1"))
    #backstage.select_max_id("income", "income_id")
    #backstage.del_data(1, flag=True)
    #backstage.update_data(phone_num="13059548593", email="13059548593#sina.com", password="345", id="1")