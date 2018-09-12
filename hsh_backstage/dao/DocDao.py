# coding=UTF-8
#根据搜索内容查询产品分页
from util import Resp
from util.BaseDao import executeQuery
from util.Util import isblank
def SearchDoc(search_text, page):
    params = []
    sql = """ SELECT ha.id, ha.doc_title, ha.doc_url, (SELECT GROUP_CONCAT(hpd.product_name) FROM hsh_product_doc h INNER JOIN hsh_product hpd 
            ON h.product_id=hpd.id WHERE h.doc_id=ha.id) product_name FROM hsh_doc ha """ 
    if isblank(search_text):
        sql = sql + "WHERE ha.doc_title like %s or ha.doc_url like %s "
        params.append(search_text)
        params.append(search_text)
    sql = sql + "GROUP BY id limit %s, %s "
    params.append((int(page)-1) * Resp.PAGESIZE)
    params.append(Resp.PAGESIZE)
    return executeQuery(sql, params, "")

#根据搜索内容查询产品数量
def SearchDocCount(search_text):
    params = []
    sql = " SELECT count(*)count from hsh_doc where 1=1 " 
    if isblank(search_text):
        sql = sql + " and doc_url like %s or doc_title like %s "
        params.append(search_text)
        params.append(search_text)
    return executeQuery(sql, params, "json")
