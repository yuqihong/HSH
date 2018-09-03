# coding=UTF-8
from util.BaseDao import executeUpdate, executeQuery
from hsh_backstage.dao import SpareDao
from util import Resp

#addSpare
def addSpare(dataJson):
    params = []
    sql = " insert into hsh_spare("
    if(dataJson.get("spare_description")!='' and dataJson.get("spare_description")!=None):
        sql = sql + "spare_description,"
    if(dataJson.get("spare_product_pn")!='' and dataJson.get("spare_product_pn")!=None):
        sql = sql + "spare_product_pn,"
    if(dataJson.get("spare_substitue_pn")!='' and dataJson.get("spare_substitue_pn")!=None):
        sql = sql + "spare_substitue_pn,"
    if(dataJson.get("spare_type_id")!='' and dataJson.get("spare_type_id")!=None):
        sql = sql + "spare_type_id,"
    if(dataJson.get("spare_pn")!='' and dataJson.get("spare_pn")!=None):
        sql = sql + "spare_pn"
    sql = sql + ") values("
     
    if(dataJson.get("spare_description")!='' and dataJson.get("spare_description")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("spare_description"))
    if(dataJson.get("spare_product_pn")!='' and dataJson.get("spare_product_pn")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("spare_product_pn"))
    if(dataJson.get("spare_substitue_pn")!='' and dataJson.get("spare_substitue_pn")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("spare_substitue_pn"))
    if(dataJson.get("spare_type_id")!='' and dataJson.get("spare_type_id")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("spare_type_id"))
    if(dataJson.get("spare_pn")!='' and dataJson.get("spare_pn")!=None):
        sql = sql + "%s"
        params.append(dataJson.get("spare_pn"))
    sql = sql + ")"
    return executeUpdate(sql, params)

#获取所有spare type的信息
def getSpareTypeList():
    params = []
    sql = "SELECT id, spare_type_name from hsh_spare_type"
    return executeQuery(sql, params, "")

#保存alertAndproduct中间表信息
def addSpareAndProduct(addSpareRow, product_id):
    params = []
    sql = " insert into hsh_product_spare("
    if(addSpareRow!='' and addSpareRow!=None):
        sql = sql + "spare_id,"
    if(product_id!='' and product_id!=None):
        sql = sql + "product_id"
    sql = sql + ") values("
     
    if(addSpareRow!='' and addSpareRow!=None):
        sql = sql + "%s,"
        params.append(addSpareRow)
    if(product_id!='' and product_id!=None):
        sql = sql + "%s)"
        params.append(product_id)
    return executeUpdate(sql, params)

#查找Alert
def getSpareList(search_text, page):
    data = {}
    count = SpareDao.SearchSpareCount(search_text)
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        if int(data["count"]) % Resp.PAGESIZE==0:
            data["pageSize"] = int(data["count"]) / Resp.PAGESIZE
        else:
            data["pageSize"] = int(int(data["count"]) / Resp.PAGESIZE) + 1
        data["list"] = SpareDao.SearchSpare(search_text, page)
    return data

#根据id获取spare信息
def getUpdateSpare(spare_id):
    params = []
    sql = """ select ha.id, ha.spare_pn, ha.spare_description, ha.spare_product_pn, ha.spare_substitue_pn,(select hpd.id from hsh_product_spare h inner join hsh_product hpd on h.product_id=hpd.id  
                where h.spare_id=ha.id) product_id , (select ty.id from hsh_spare_type ty
                where ty.id = ha.spare_type_id)type_id from hsh_spare ha where ha.id = %s"""
    params.append(spare_id)
    return executeQuery(sql, params, "")

#更新中间表
def updateProductIdBySpareId(spare_id, product_id):
    params = []
    sql = """ update hsh_product_spare set product_id = %s where spare_id = %s """
    params.append(product_id)
    params.append(spare_id)
    return executeUpdate(sql, params)
#更新spare
def updateSpare(dataJson):
    params = []
    sql = """ update hsh_spare set spare_pn = %s, spare_description = %s, spare_product_pn = %s, spare_substitue_pn = %s,spare_type_id = %s """
    params.append(dataJson.get("spare_pn"))
    params.append(dataJson.get("spare_description"))
    params.append(dataJson.get("spare_product_pn"))
    params.append(dataJson.get("spare_substitue_pn"))
    params.append(dataJson.get("spare_type_id"))
    sql = sql + " where id = %s"
    params.append(dataJson.get("spare_id"))
    return executeUpdate(sql, params)

#根据spare_id删除中间表信息
def delModdinBySpareId(spare_id):
    params = []
    sql = """ DELETE from hsh_product_spare  where spare_id = %s """
    params.append(spare_id)
    return executeUpdate(sql, params)

#根据alert_id删除alert信息
def delSpare(spare_id):
    params = []
    sql = """ DELETE from hsh_spare  where id = %s """
    params.append(spare_id)
    return executeUpdate(sql, params)

#根据spareId查询中间表信息
def getModdBySpareId(spare_id):
    params = []
    sql = " SELECT product_id from hsh_product_spare where spare_id = %s"
    params.append(spare_id)
    return executeQuery(sql, params, "")