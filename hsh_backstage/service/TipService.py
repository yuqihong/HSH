# coding=UTF-8
from util.BaseDao import executeUpdate, executeQuery
from hsh_backstage.dao import TipDao
from util import Resp

#添加tip信息
def addTip(dataJson):
    params = []
    sql = " insert into hsh_tip("
    if(dataJson.get("tip_detail")!='' and dataJson.get("tip_detail")!=None):
        sql = sql + "tip_detail"
    sql = sql + ") values("  
    if(dataJson.get("tip_detail")!='' and dataJson.get("tip_detail")!=None):
        sql = sql + "%s)"
        params.append(dataJson.get("tip_detail"))
    return executeUpdate(sql, params)

#获取所有产品的信息
def getTheirProductTip():
    params = []
    sql = "SELECT id, product_name, product_long_name  from hsh_product"
    return executeQuery(sql, params, "")

#保存tipAndproduct中间表信息
def addTipAndProduct(addTipRow, product_id):
    params = []
    sql = " insert into hsh_product_tip("
    if(addTipRow!='' and addTipRow!=None):
        sql = sql + "tip_id,"
    if(product_id!='' and product_id!=None):
        sql = sql + "product_id"
    sql = sql + ") values("
     
    if(addTipRow!='' and addTipRow!=None):
        sql = sql + "%s,"
        params.append(addTipRow)
    if(product_id!='' and product_id!=None):
        sql = sql + "%s)"
        params.append(product_id)
    return executeUpdate(sql, params)

#查找tip
def getTipList(search_text, page):
    data = {}
    count = TipDao.SearchTipCount(search_text)
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        if int(data["count"]) % Resp.PAGESIZE==0:
            data["pageSize"] = int(data["count"]) / Resp.PAGESIZE
        else:
            data["pageSize"] = int(int(data["count"]) / Resp.PAGESIZE) + 1
        data["list"] = TipDao.SearchTip(search_text, page)
    return data

#根据id获取tip信息
def getUpdateTip(tip_id):
    params = []
    sql = """ SELECT *,(SELECT hpd.id FROM hsh_product_tip h INNER JOIN hsh_product hpd ON h.product_id=hpd.id  
                WHERE h.tip_id=ha.id) product_id FROM hsh_tip ha WHERE ha.id = %s"""
    params.append(tip_id)
    return executeQuery(sql, params, "")

#更新中间表
def updateProductIdByTipId(tip_id, product_id):
    params = []
    sql = """ update hsh_product_tip set product_id = %s where tip_id = %s """
    params.append(product_id)
    params.append(tip_id)
    return executeUpdate(sql, params)
#更新tip
def updateTip(dataJson):
    params = []
    sql = """ update hsh_tip set  tip_detail = %s where id = %s """
    params.append(dataJson.get("tip_detail"))
    params.append(dataJson.get("tip_id"))
    return executeUpdate(sql, params)

#根据tip_id删除中间表信息
def delModdinByTipId(tip_id):
    params = []
    sql = """ DELETE from hsh_product_tip  where tip_id = %s """
    params.append(tip_id)
    return executeUpdate(sql, params)

#根据tip_id删除tip信息
def delTip(tip_id):
    params = []
    sql = """ DELETE from hsh_tip  where id = %s """
    params.append(tip_id)
    return executeUpdate(sql, params)

#根据tipId查询中间表信息
def getModdByTipId(tip_id):
    params = []
    sql = " SELECT product_id from hsh_product_tip where tip_id = %s"
    params.append(tip_id)
    return executeQuery(sql, params, "")
