# coding=UTF-8
from util.BaseDao import executeUpdate, executeQuery
from hsh_backstage.dao import AlertDao
from util import Resp
from selenium.webdriver.common import alert

#添加Alert信息
def addAlert(dataJson):
    params = []
    sql = " insert into hsh_alert("
    if(dataJson.get("alert_number")!='' and dataJson.get("alert_number")!=None):
        sql = sql + "alert_number,"
    if(dataJson.get("alert_detail")!='' and dataJson.get("alert_detail")!=None):
        sql = sql + "alert_detail"
    sql = sql + ") values("
     
    if(dataJson.get("alert_number")!='' and dataJson.get("alert_number")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("alert_number"))
    if(dataJson.get("alert_detail")!='' and dataJson.get("alert_detail")!=None):
        sql = sql + "%s)"
        params.append(dataJson.get("alert_detail"))
    return executeUpdate(sql, params)

#获取所有产品的信息
def getTheirProductList():
    params = []
    sql = "SELECT id, product_name, product_long_name  from hsh_product"
    return executeQuery(sql, params, "")

#保存alertAndproduct中间表信息
def addAlertAndProduct(addAlertRow, product_id):
    params = []
    sql = " insert into hsh_product_alert("
    if(addAlertRow!='' and addAlertRow!=None):
        sql = sql + "alert_id,"
    if(product_id!='' and product_id!=None):
        sql = sql + "product_id"
    sql = sql + ") values("
     
    if(addAlertRow!='' and addAlertRow!=None):
        sql = sql + "%s,"
        params.append(addAlertRow)
    if(product_id!='' and product_id!=None):
        sql = sql + "%s)"
        params.append(product_id)
    return executeUpdate(sql, params)

#查找Alert
def getAlertList(search_text, page):
    data = {}
    count = AlertDao.SearchAlertCount(search_text)
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        if int(data["count"]) % Resp.PAGESIZE==0:
            data["pageSize"] = int(data["count"]) / Resp.PAGESIZE
        else:
            data["pageSize"] = int(int(data["count"]) / Resp.PAGESIZE) + 1
        data["list"] = AlertDao.SearchAlert(search_text, page)
    return data

#根据id获取alert信息
def getUpdateAlert(alert_id):
    params = []
    sql = """ select *,(select hpd.id from hsh_product_alert h inner join hsh_product hpd on h.product_id=hpd.id  
                where h.alert_id=ha.id) product_id from hsh_alert ha where ha.id = %s"""
    params.append(alert_id)
    return executeQuery(sql, params, "")

#更新中间表
def updateProductIdByAlertId(alert_id, product_id):
    params = []
    sql = """ update hsh_product_alert set product_id = %s where alert_id = %s """
    params.append(product_id)
    params.append(alert_id)
    return executeUpdate(sql, params)
#更新alert
def updateAlert(dataJson):
    params = []
    sql = """ update hsh_alert set alert_number = %s, alert_detail = %s where id = %s """
    params.append(dataJson.get("alert_number"))
    params.append(dataJson.get("alert_detail"))
    params.append(dataJson.get("alert_id"))
    return executeUpdate(sql, params)

#根据alert_id删除中间表信息
def delModdinByAlertId(alert_id):
    params = []
    sql = """ DELETE from hsh_product_alert  where alert_id = %s """
    params.append(alert_id)
    return executeUpdate(sql, params)

#根据alert_id删除alert信息
def delAlert(alert_id):
    params = []
    sql = """ DELETE from hsh_alert  where id = %s """
    params.append(alert_id)
    return executeUpdate(sql, params)


#根据alertId查询中间表信息
def getModdByAlertId(alert_id):
    params = []
    sql = " SELECT product_id from hsh_product_alert where alert_id = %s"
    params.append(alert_id)
    return executeQuery(sql, params, "")
