# coding=UTF-8
from util.BaseDao import executeQuery

#查询所有产品
def getCurrentSystemProduct():
    sql = """ select c.id as category_id, c.category_name,p.id as product_id, GROUP_CONCAT(p.product_name)product_name, 
        p.product_long_name, p.product_eol, product_view_url, p.hsh_property_id, p.create_time
        from hsh_category as c RIGHT JOIN hsh_product as p ON
        c.id = p.hsh_category_id GROUP BY c.category_name, product_eol """
    return executeQuery(sql, [], "") 

#查询所有产品2
def getCurrentSystemProduct_EOL_1():
    sql = """ select c.id as category_id, c.category_name,p.id as product_id, GROUP_CONCAT(p.product_name)product_name, 
        p.product_long_name, p.product_eol, product_view_url, p.hsh_property_id, p.create_time
        from hsh_category as c RIGHT JOIN hsh_product as p ON
        c.id = p.hsh_category_id where p.product_eol = 1 GROUP BY c.category_name, product_eol """
    return executeQuery(sql, [], "") 

#查询所有产品3
def getCurrentSystemProduct_EOL_0():
    sql = """ select c.id as category_id, c.category_name,p.id as product_id, GROUP_CONCAT(p.product_name)product_name, 
        p.product_long_name, p.product_eol, product_view_url, p.hsh_property_id, p.create_time
        from hsh_category as c RIGHT JOIN hsh_product as p ON
        c.id = p.hsh_category_id where p.product_eol = 0 GROUP BY c.category_name, product_eol """
    return executeQuery(sql, [], "") 
#查询所有产品数量
def getProductCount():
    sql = """ select count(*)count
            from hsh_category as c RIGHT JOIN hsh_product as p ON
            c.id = p.hsh_category_id """
    return executeQuery(sql, [], "json") 

