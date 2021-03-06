#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 完成vulnerability表中type为3的数据的填充
# 取出cnvd表中剩下的cnvd（moved为0），再将其存储至vulnerability表
# 至此，三种类型的vulnerability存储完毕

# 注意，cnvd表中有重复的（CNVD号重复，但具体内容不重复）

import MySQLdb
import json
import sys
import os

db = MySQLdb.connect(
    host = "localhost", port = 3306, user = "root", 
    passwd = "123456", db = "net_test", charset = "utf8"
    )

cursor = db.cursor()

def err_log():
    print "error"
    error_info = sys.exc_info()
    if len(error_info) > 1:
        print(str(error_info[0]) + ' ' + str(error_info[1]))

def insert3vul(i):
    # i是当前vulnerability表中没有的CNVDId
    sql = """
    insert into vulnerability (`cnvdId`, `type`) values ("{cnvd}", 3);
    """.format(cnvd = i)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        err_log()

try:
    cursor.execute("""
    select distinct number from cnvd where moved = 0;
    """)
    data = cursor.fetchall()
    count = 0
    for item in data: # 待插入vulnerability的数据
        count += 1
        print item[0]
        insert3vul(item[0])
    print count
except:
    err_log()

db.close()
