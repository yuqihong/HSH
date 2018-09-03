# coding=UTF-8
#根据搜索内容查询产品分页
from util import Resp
from util.BaseDao import executeQuery
from util.Util import isblank
def SearchAlert(search_text, page):
    params = []
    sql = """ select *,(select GROUP_CONCAT(hpd.product_name) from hsh_product_alert h inner join hsh_product hpd on h.product_id=hpd.id  where h.alert_id=ha.id) product_name
                from hsh_alert ha  """ 
    if isblank(search_text):
        sql = sql + " and ha.alert_detail like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or ha.alert_number like %s "
        params.append(search_text)
    sql = sql + " GROUP BY ha.id limit %s,%s"
    params.append((int(page)-1) * Resp.PAGESIZE)
    params.append(Resp.PAGESIZE)
    return executeQuery(sql, params, "")

#根据搜索内容查询产品数量
def SearchAlertCount(search_text):
    params = []
    sql = " SELECT count(*)count from hsh_alert c where 1=1 " 
    if isblank(search_text):
        sql = sql + " and c.alert_detail like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or c.alert_number like %s "
        params.append(search_text)
    return executeQuery(sql, params, "json")
