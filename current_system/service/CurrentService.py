# coding=UTF-8
from util.BaseDao import executeQuery
from current_system.dao import CurrentDao

def getCurrentSystemCategory():
    sql = " SELECT * from hsh_category "
    return executeQuery(sql, [], "JSON")

def getCurrentSystemProduct():
    data = {}
    count = CurrentDao.getProductCount()
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        data["list"] = CurrentDao.getCurrentSystemProduct()
    return data

def getCurrentSystemProduct_EOL_0():
    data = {}
    count = CurrentDao.getProductCount()
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        data["list"] = CurrentDao.getCurrentSystemProduct_EOL_0()
    return data

def getCurrentSystemProduct_EOL_1():
    data = {}
    count = CurrentDao.getProductCount()
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        data["list"] = CurrentDao.getCurrentSystemProduct_EOL_1()
    return data

def selectCurrentSystemByProductName(product_name):
    params = []
    sql = """ SELECT prop.id as property_id, prop.code_name, prop.ga_date, 
        prop.max_cache, prop.product_hight, prop.bandwidth, prop.system_architecture, prop.data_sheet,
        prop.is_show, prod.id as product_id, prod.product_name, prod.product_long_name, prod.product_eol,
        prod.product_view_url, prod.create_time
        from hsh_property as prop RIGHT JOIN hsh_product as prod ON
        prod.hsh_property_id = prop.id
        where prop.id in 
        (select hsh_property_id from hsh_product where product_name=%s) """
    params.append(product_name)
    return executeQuery(sql, params, "")
