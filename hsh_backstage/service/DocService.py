# coding=UTF-8
from util.BaseDao import executeUpdate, executeQuery
from hsh_backstage.dao import DocDao
from util import Resp

#添加Doc信息
def addDoc(dataJson):
    params = []
    data = [dataJson["doc_title"], dataJson["doc_url"]]
    sql = " insert INTO hsh_doc (doc_title, doc_url) VALUES (%s, %s) "
    params.append(dataJson["doc_title"])
    params.append(dataJson["doc_url"])
    return executeUpdate(sql, data)

#获取所有产品的信息
def getProductList():
    params = []
    sql = " SELECT id, product_name, product_long_name FROM hsh_product "
    return executeQuery(sql, params, "")

#保存docAndproduct中间表信息
def addDocAndProduct(doc_id, product_id):
    data = [doc_id, product_id]
    sql = """ INSERT INTO hsh_product_doc (doc_id, product_id) VALUES (%s, %s) """
    return executeUpdate(sql, data)

#查找Doc
def getDocList(search_text, page):
    data = {}
    count = DocDao.SearchDocCount(search_text)
    data["count"] = int(count[0]["count"])
    if data["count"] > 0:
        if data["count"] % Resp.PAGESIZE == 0:
            data["pageSize"] = data["count"] / Resp.PAGESIZE
        else:
            data["pageSize"] = int(data["count"] / Resp.PAGESIZE) + 1
        data["list"] = DocDao.SearchDoc(search_text, page)
    return data

#通过doc_title,doc_url查找doc_id
def getDocid(doc_title, doc_url):
    params = [doc_title, doc_url]
    sql = " SELECT id, doc_title, doc_url FROM hsh_doc WHERE doc_title=%s AND doc_url=%s "
    return executeQuery(sql, params, "")

#根据id获取doc信息
def getUpdateDoc(doc_id):
    params = [doc_id]
    sql = """ SELECT id, doc_title, doc_url, (SELECT hpd.id FROM hsh_product_doc h INNER JOIN hsh_product hpd on h.product_id=hpd.id  
                WHERE h.doc_id=ha.id) AS product_id from hsh_doc ha where ha.id=%s """
    return executeQuery(sql, params, "")

#更新中间表
def updateProductIdByDocId(product_id, doc_id):
    params = [product_id, doc_id]
    sql = """ UPDATE hsh_product_doc SET product_id=%s WHERE doc_id=%s """
    return executeUpdate(sql, params)

#更新doc
def updateDoc(dataJson):
    params = [dataJson["doc_title"], dataJson["doc_url"], dataJson["doc_id"]]
    sql = """ UPDATE hsh_doc SET doc_title=%s, doc_url=%s WHERE id=%s """
    return executeUpdate(sql, params)

#根据doc_id删除中间表信息
def delModdinByDocId(doc_id):
    params = [doc_id]
    sql = """ DELETE FROM hsh_product_doc WHERE doc_id=%s """
    return executeUpdate(sql, params)

#根据doc_id删除doc信息
def delDoc(doc_id):
    params = [doc_id]
    sql = """ DELETE FROM hsh_doc WHERE id=%s """
    return executeUpdate(sql, params)

#根据docId查询中间表信息
def getModdByDocId(doc_id):
    params = [doc_id]
    sql = " SELECT product_id from hsh_product_doc where doc_id=%s "
    return executeQuery(sql, params, "")

