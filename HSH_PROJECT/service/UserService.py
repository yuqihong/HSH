# coding=utf-8
from util.BaseDao import executeQuery

# 根据用户名和密码查询用户信息
def getUserLogin(user_name, user_pass):
    # 准备sql语句
    sql="select user_name,user_pass from hsh_user where user_name=%s and user_pass=%s";
    value = []
    value.append(user_name)
    value.append(user_pass)
    # 参数一: sql语句
    # 参数二: 参数值
    # 参数三: 返回的数据类型
    return executeQuery(sql,value,"")

# 根据用户名查询用户权限信息
def getUserPermission(user_name):
    sql = " select * from hsh_user u where u.user_name = %s "
    return executeQuery(sql,[user_name],"")