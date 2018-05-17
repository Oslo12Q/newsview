# -*- coding:utf-8 -*-
import pymysql as mdb

# 数据库的配置信息
mysql_conf = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'passwd': 'nicaicai',
    'charset': 'utf8',
    'db': 'jskc',
}


# 连接数据库
class Database(object):
    def __init__(self):
        self.con = mdb.connect(host=mysql_conf['host'], user=mysql_conf['user'], passwd=mysql_conf['passwd'],
                               db=mysql_conf['db'], charset=mysql_conf['charset'])

    # 批量插入数据
    def insert_batch_data(self, query, list_data):
        cur = self.con.cursor()
        cur.executemany(query, list_data)
        self.con.commit()
        self.con.close()

    # 单个插入数据
    def insert_data(self, query, data):
        cur = self.con.cursor()
        cur.execute(query, data)
        self.con.commit()
        self.con.close()

    # 获取数据
    def select_data(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        self.con.close()
        return rows
