# coding=UTF-8
#根据搜索内容查询产品分页
from util import Resp
from util.BaseDao import executeQuery
from util.Util import isblank
def SearchSpare(search_text, page):
    params = []
    sql = """ select ha.id, ha.spare_pn, ha.spare_description, ha.spare_product_pn, ha.spare_substitue_pn,(select GROUP_CONCAT(hpd.product_name) from hsh_product_spare h inner join hsh_product hpd on h.product_id=hpd.id  
            where h.spare_id=ha.id) product_name , (select GROUP_CONCAT(ty.spare_type_name) from hsh_spare_type ty
            where ty.id = ha.spare_type_id)type_name from hsh_spare ha 
            """ 
    if isblank(search_text):
        sql = sql + " and ha.spare_pn like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or ha.spare_product_pn like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or ha.spare_substitue_pn like %s "
        params.append(search_text)
    sql = sql + " GROUP BY ha.id limit %s,%s"
    params.append((int(page)-1) * Resp.PAGESIZE)
    params.append(Resp.PAGESIZE)
    return executeQuery(sql, params, "")

#根据搜索内容查询产品数量
def SearchSpareCount(search_text):
    params = []
    sql = " SELECT count(*)count from hsh_spare s where 1=1 " 
    if isblank(search_text):
        sql = sql + " and s.spare_pn like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or s.spare_product_pn like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or s.spare_substitue_pn like %s "
        params.append(search_text)
    return executeQuery(sql, params, "json")
