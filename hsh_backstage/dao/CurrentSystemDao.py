# coding=UTF-8
#根据搜索内容查询产品分页
from util import Resp
from util.BaseDao import executeQuery
from util.Util import isblank
def SearchProduct(search_text, page):
    params = []
    sql = """ SELECT c.id as category_id, category_name, p.id as product_id
            , p.product_name, p.product_long_name, p.hsh_property_id, p.product_eol
            ,p.product_view_url, p.create_time as create_time from hsh_category c INNER JOIN  hsh_product p ON c.id = p.hsh_category_id 
            where 1=1 """ 
    if isblank(search_text):
        sql = sql + " and c.category_name like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or p.product_name like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or p.product_long_name like %s "
        params.append(search_text)
    sql = sql + " ORDER BY p.create_time DESC limit %s,%s"
    params.append((int(page)-1) * Resp.PAGESIZE)
    params.append(Resp.PAGESIZE)
    return executeQuery(sql, params, "")

#根据搜索内容查询产品数量
def SearchProductCount(search_text):
    params = []
    sql = " SELECT count(*) count from hsh_category c INNER JOIN  hsh_product p ON c.id = p.hsh_category_id where 1=1 " 
    if isblank(search_text):
        sql = sql + " and c.category_name like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or p.product_name like %s "
        params.append(search_text)
    if isblank(search_text):
        sql = sql + " or p.product_long_name like %s "
        params.append(search_text)
    return executeQuery(sql, params, "json")