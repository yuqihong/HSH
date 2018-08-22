# coding=UTF-8
from util.BaseDao import executeUpdate, executeQuery
from unicodedata import category
from util.Util import isblank
from re import search
from util import Resp
from hsh_backstage.dao import CurrentSystemDao

#添加产品信息
def addProduct_insert(dataJson, addPrpertyRow):
    params = []
    sql = " insert into hsh_product("
    if(dataJson.get("product_long_name")!='' and dataJson.get("product_long_name")!=None):
        sql = sql + "product_long_name,"
    if(addPrpertyRow!=0):
        sql = sql + "hsh_property_id,"
    if(dataJson.get("product_eol")!='' and dataJson.get("product_eol")!=None):
        sql = sql + "product_eol,"
    if(dataJson.get("hsh_category_id")!='' and dataJson.get("hsh_category_id")!=None):
        sql = sql + "hsh_category_id, "
         
    sql = sql + " product_name) values("
     
    if(dataJson.get("product_long_name")!='' and dataJson.get("product_long_name")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("product_long_name"))
    if(addPrpertyRow!=0):
        sql = sql + "%s,"
        params.append(addPrpertyRow)
    if(dataJson.get("product_eol")!='' and dataJson.get("product_eol")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("product_eol"))
    if(dataJson.get("hsh_category_id")!='' and dataJson.get("hsh_category_id")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("hsh_category_id"))
    sql = sql + "%s)"
    params.append(dataJson.get("product_name"))
    print(sql)
    return executeUpdate(sql, params)

#添加产品信息
def addProduct_update(dataJson, addPrpertyRow):
    params = []
    sql = " update hsh_product set "
    if(dataJson.get("product_long_name")!='' and dataJson.get("product_long_name")!=None):
        sql = sql + "product_long_name = %s,"
        params.append(dataJson.get("product_long_name"))
    if(addPrpertyRow!=0):
        sql = sql + "hsh_property_id = %s,"
        params.append(addPrpertyRow)
    if(dataJson.get("product_eol")!='' and dataJson.get("product_eol")!=None):
        sql = sql + "product_eol = %s,"
        params.append(dataJson.get("product_eol"))
    if(dataJson.get("hsh_category_id")!='' and dataJson.get("hsh_category_id")!=None):
        sql = sql + "hsh_category_id = %s, "
        params.append(dataJson.get("hsh_category_id"))
        
    sql = sql + " product_name = %s"
    params.append(dataJson.get("product_name"))
    sql = sql + " where id = %s"
    params.append(dataJson.get("product_id"))
    print(sql)
    return executeUpdate(sql, params)
#添加产品属性信息
def addPrperty(dataJson):
    params = []
    sql = " insert into hsh_property("
    if(dataJson.get("code_name")!='' and dataJson.get("code_name")!=None):
        sql = sql + "code_name,"
    if(dataJson.get("ga_date")!='' and dataJson.get("ga_date")!=None):
        sql = sql + "ga_date,"
    if(dataJson.get("max_cache")!='' and dataJson.get("max_cache")!=None):
        sql = sql + "max_cache,"
    if(dataJson.get("product_hight")!='' and dataJson.get("product_hight")!=None):
        sql = sql + "product_hight,"
    if(dataJson.get("bandwidth")!='' and dataJson.get("bandwidth")!=None):
        sql = sql + "bandwidth,"
    if(dataJson.get("system_architecture")!='' and dataJson.get("system_architecture")!=None):
        sql = sql + "system_architecture,"
    if(dataJson!='' and dataJson!=None):
        sql = sql + "data_sheet,"
        
    sql = sql + " is_show) values("
    
    if(dataJson.get("code_name")!='' and dataJson.get("code_name")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("code_name"))
    if(dataJson.get("ga_date")!='' and dataJson.get("ga_date")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("ga_date"))
    if(dataJson.get("max_cache")!='' and dataJson.get("max_cache")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("max_cache"))
    if(dataJson.get("product_hight")!='' and dataJson.get("product_hight")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("product_hight"))
    if(dataJson.get("bandwidth")!='' and dataJson.get("bandwidth")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("bandwidth"))
    if(dataJson.get("system_architecture")!='' and dataJson.get("system_architecture")!=None):
        sql = sql + "%s,"
        params.append(dataJson.get("system_architecture"))
    if(dataJson!='' and dataJson!=None):
        sql = sql + "%s,"
        params.append(dataJson)
    sql = sql + "%s)"
    params.append(dataJson.get("is_show"))
    print(sql)
    return executeUpdate(sql, params)

#删除产品属性信息
def delProperty(property_id):
    params = []
    sql = " DELETE from hsh_property where id=%s "
    params.append(property_id)
    return executeUpdate(sql, params)
    
#删除产品信息
def delProduct(product_id):
    params = []
    sql = " DELETE from hsh_product where id=%s "
    params.append(product_id)
    return executeUpdate(sql, params)

#修改产品信息
def updateProduct(dataJson):
    params = []
    sql = """ update hsh_product set product_name = %s, product_long_name = %s , product_eol = %s ,
     hsh_category_id = %s where id = %s """
    params.append(dataJson.get("product_name"))
    params.append(dataJson.get("product_long_name"))
    params.append(dataJson.get("product_eol"))
    params.append(dataJson.get("hsh_category_id"))
    params.append(dataJson.get("product_id"))
    return executeUpdate(sql, params)

#修改产品属性信息
def updateProperty(dataJson, property_id):
    params = []
    sql = """ update hsh_property set code_name = %s, ga_date = %s , max_cache = %s , product_hight = %s, 
    bandwidth = %s, system_architecture = %s, data_sheet = %s,is_show = %s where id = %s """
    params.append(dataJson.get("code_name"))
    params.append(dataJson.get("ga_date"))
    params.append(dataJson.get("max_cache"))
    params.append(dataJson.get("product_hight"))
    params.append(dataJson.get("bandwidth"))
    params.append(dataJson.get("system_architecture"))
    params.append(dataJson)
    params.append(dataJson.get("is_show"))
    params.append(property_id)
    return executeUpdate(sql, params)

#获取所有的分类
def getCategoryList():
    sql = " SELECT id, category_name from hsh_category "
    return executeQuery(sql, [], "JSON")

#根据分类id查询分类
def getPropertyById(product_id):
    params = []
    sql = " select hsh_property_id from hsh_product where id=%s "
    params.append(product_id)
    return executeQuery(sql, params, "")

#根据产品id查询产品信息
def getProductById(product_id):
    params = []
    sql = """ SELECT prop.id as property_id, prop.code_name, prop.ga_date, prop.max_cache,prop.product_hight,
    prop.bandwidth, prop.system_architecture, prop.data_sheet, prop.is_show, prod.id as product_id, prod.product_name, prod.product_long_name,
    prod.product_eol, prod.product_view_url, prod.hsh_category_id, prod.create_time
    from hsh_property prop right join hsh_product prod on prop.id = prod.hsh_property_id 
    where prod.id =%s """
    params.append(product_id)
    return executeQuery(sql, params, "")
#查找产品
def getCurrentSystemList(search_text, page):
    data = {}
    count = CurrentSystemDao.SearchProductCount(search_text)
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        if int(data["count"]) % Resp.PAGESIZE==0:
            data["pageSize"] = int(data["count"]) / Resp.PAGESIZE
        else:
            data["pageSize"] = int(int(data["count"]) / Resp.PAGESIZE) + 1
        data["list"] = CurrentSystemDao.SearchProduct(search_text, page)
    return data
def getEOLSystemList(search_text, page):
    data = {}
    count = CurrentSystemDao.SearchEOLProductCount(search_text)
    data["count"] = count[0]["count"]
    if int(data["count"])>0:
        if int(data["count"]) % Resp.PAGESIZE==0:
            data["pageSize"] = int(data["count"]) / Resp.PAGESIZE
        else:
            data["pageSize"] = int(int(data["count"]) / Resp.PAGESIZE) + 1
        data["list"] = CurrentSystemDao.SearchEOLProduct(search_text, page)
    return data
    
#根据产品id返回产品属性的id
def getPropertyIdByProductId(product_id):
    params = []
    sql = " select hsh_property_id from hsh_product where id = %s "
    params.append(product_id)
    return executeQuery(sql, params, "")

#跟据product_id将图片url保存
def saveCurrentSystemImage(image_url):
    params = []
    sql = " insert into hsh_product("
    if(image_url!='' and image_url!=None):
        sql = sql + "product_view_url"
    
    sql = sql + ") values("
    
    if(image_url!='' and image_url!=None):
        sql = sql + "%s)"
        params.append(image_url)
    return executeUpdate(sql, params)

#跟据product_id将图片url修改
def updateCurrentSystemImage(image_url, product_id):
    params = []
    sql = " update hsh_product set product_view_url = %s where id = %s "
    params.append(image_url)
    params.append(product_id)
    return executeUpdate(sql, params)