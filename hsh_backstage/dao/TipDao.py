# coding=UTF-8

from util import Resp
from util.BaseDao import executeQuery
from util.Util import isblank
#根据搜索内容查询产品分页
def SearchTip(search_text, page):
    params = []
    sql = """ SELECT hsh_tip.`id` AS tip_id,hsh_tip.`tip_detail`,hsh_product.`product_name`
                FROM hsh_tip 
                    LEFT JOIN hsh_product_tip ON hsh_tip.`id`=hsh_product_tip.`tip_id`
                    LEFT JOIN hsh_product ON hsh_product.`id`= hsh_product_tip.`product_id`
                where 1=1""" 
    if isblank(search_text):
        sql = sql + " and hsh_tip.tip_detail like %s "
        params.append(search_text)
    sql = sql + " GROUP BY hsh_tip.id limit %s,%s"
    params.append((int(page)-1) * Resp.PAGESIZE)
    params.append(Resp.PAGESIZE)
    return executeQuery(sql, params, "")

#根据搜索内容查询产品数量
def SearchTipCount(search_text):
    params = []
    sql = " SELECT count(*)count from hsh_tip c where 1=1 " 
    if isblank(search_text):
        sql = sql + " and c.tip_detail like %s "
        params.append(search_text)
    return executeQuery(sql, params, "")
