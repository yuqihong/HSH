# coding=utf-8

import pymysql
from django.db import connection
import json
from builtins import Exception
import sys

# 通用的查询方法
# 参数一: sql语句
# 参数二: 参数值
# 参数三: 返回的数据类型
def executeQuery(sql, params, data_type):
    result = []
    # 获取mysql操作的方法
    cur=connection.cursor()
    try:
        # 执行查询语句
        if(len(params)>0):
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        # 得到域的名字（列名）
        index = cur.description
        data = cur.fetchall()
        # 定义一个数组
        #  fetchall 获取查询结果
        column_list = []
        data_list = []
        for i in index:
            column_list.append(i[0])
        for row in data:
            result = {}
            for cl in range(0,len(column_list)):
                result[column_list[cl]] = str(row[cl])
            data_list.append(result)
        cur.close
    except:
        cur.close()
        print(sys.exc_info())
    else:
        cur.close()
    if(data_type=='JSON'):
        return json.dumps(data_list,ensure_ascii=False);
    else:
        return data_list
# 通用的增删改方法
# 参数一: sql语句
# 参数二: 参数值
def executeUpdate(sql, params):
    row = 0
    # 获取mysql操作的方法
    cur=connection.cursor()
    try:
        if(len(params)>0):
            row = cur.execute(sql, params)
        else:
            row = cur.execute(sql, params)
        if(sql.index("insert")>=0 or sql.index("INSERT")>=0):
            row = cur.lastrowid
        cur.close
    except:
        cur.close()
        print(sys.exc_info())
    return row