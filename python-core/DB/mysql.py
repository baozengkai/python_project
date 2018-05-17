# -*- coding:utf-8 -*-
import pymysql
"""
    Mysql操作:
        1.Mysql连接并查询、打印其版本信息
        2.查询一个表中所有的数据
        3.删除表以及建立表
        4.插入数据
        5.更新数据
        6.删除数据
"""

# 连接数据库
db = pymysql.connect("192.168.84.150","root","123456","BAOZENGKAI",use_unicode=True,charset="utf8")


# 创建一个游标对象
cursor = db.cursor()

# 使用execute()方法执行SQL查询、fetchone()获取单条的数据信息
# ----------------1.查询版本信息-----------------------------------
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("DataBase Version:%s" %data)

# 使用fetchall()获取所有的数据
# ----------------2.查询表中数据-----------------------------------
# cursor.execute("SELECT * FROM person")
# datas = cursor.fetchall()
# print(datas)
# print(type(datas))
# print(datas[0][4])

# ----------------3.删除表、建立表---------------------------------
# cursor.execute("DROP TABLE IF EXISTS log_event")
#
# sql = """CREATE TABLE log_event(
#             id INT NOT NULL AUTO_INCREMENT,
#             event_name VARCHAR(30) NOT NULL,
#             json_value VARCHAR(1000) NOT NULL,
#             PRIMARY  KEY(id))ENGINE=InnoDB DEFAULT CHARSET=utf8"""
# cursor.execute(sql)

# ----------------4.插入数据---------------------------------------
# json_data = '{"dataSet":"22222","index":"rainbow"}'
#
# try:
#     sql = """INSERT INTO log_event
#              (event_name,json_value)
#              VALUES('事件3号','%s')
#           """%json_data
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# ----------------5.更新数据---------------------------------------
# str = "event1"
# json_data = '{"dataSet":"11111","index":"graph"}'
#
# try:
#     sql= "UPDATE  log_event SET json_value = '%s' WHERE event_name = '%s'"%(json_data, str)
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

# ----------------6.删除数据---------------------------------------
# str = 'event2'
# try:
#     sql = "DELETE FROM log_event WHERE event_name = '%s'" %(str)
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

db.close()