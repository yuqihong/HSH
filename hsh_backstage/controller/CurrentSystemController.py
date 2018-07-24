# coding=UTF-8
from util.Util import _post, toJson
from django.http.response import HttpResponse
from hsh_backstage.service import CurrentSystemService
from util.Aop import loginVerify
from django.shortcuts import render
import json
from util import Resp, DateUtil
import os

@loginVerify
def getCurrentSystem(request):
    return render(request,'hsh_backstage/view/current_system/select.html')

@loginVerify
def addMenu(request):
    return render(request,'hsh_backstage/view/current_system/add.html')

#添加产品信息（先添加产品属性表--hsh_property）,再将添加成功的id添加到产品表中（hsh_product）
@loginVerify
def saveCurrentSystem(request):
    dataJson = json.loads(_post(request, "data"))
    #先添加产品属性表中
    addPrpertyRow = CurrentSystemService.addPrperty(dataJson)
    #再获取上面添加到的id添加到产品表中
    if(addPrpertyRow > 0):
        if(dataJson["product_id"]):
            addProductRow = CurrentSystemService.addProduct_update(dataJson, addPrpertyRow)
        else:
            addProductRow = CurrentSystemService.addProduct_insert(dataJson, addPrpertyRow)
    if addProductRow > 0:
        return HttpResponse(toJson({"state": "ok"}))
    else:
        return HttpResponse(toJson({"error": "添加失败"}))

#上传图片
def saveCurrentSystemImage(request):
    #获取前端上传的图片
    file = request.FILES.getlist('files')
    i = 0
    file_name1 = ""
    for f in file:
        name = f.name
        file_name = name.split(".")[0] + "_"+ DateUtil.time_stamp() +"."+ name.split(".")[1]
        img_path = os.path.join(Resp.IMAGEUPLOAD, file_name)
        file_name1+="/images/currentsystem_images/" + file_name+","
    #写入到文件中
        with open(img_path,'wb') as  ff:
            for item in f.chunks():
                ff.write(item)
    print(file_name1)
    saveImageRow =  CurrentSystemService.saveCurrentSystemImage(file_name1)
    #路径保存到数据库
    respJson = {}
    if saveImageRow > 0:
        respJson["product_id"] = saveImageRow
    else:
        respJson["ERROR"] = Resp.ERROR
    return HttpResponse(toJson(respJson));
#先删除hsh_product产品表，再删除hsh_property属性表
@loginVerify
def delCurrentSystem(request):
    dataJson = json.loads(_post(request, "data"))
    respJson = {}
    product_id = dataJson.get("product_id")
    propertyId = CurrentSystemService.getPropertyById(product_id)
    delProductRow = CurrentSystemService.delProduct(product_id)
    if(delProductRow > 0):
        delPropertyRow = CurrentSystemService.delProperty(propertyId[0]['hsh_property_id'])
    if(delPropertyRow > 0):
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));

#修改产品
@loginVerify
def updateCurrentSystem(request):
    dataJson = json.loads(_post(request, "data"))
    
    #先根据product_id获取产品属性Id
    pid = CurrentSystemService.getPropertyIdByProductId(dataJson.get("product_id"))
    #先修改产品属性
    property_id = pid[0]["hsh_property_id"]
    updatePropertyRow = CurrentSystemService.updateProperty(dataJson, property_id)
    if(updatePropertyRow > 0):
        updateProductRow = CurrentSystemService.updateProduct(dataJson)
    respJson = {}
    if updateProductRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));

#获取所有的分类
@loginVerify
def getCategoryList(request):
    return HttpResponse(CurrentSystemService.getCategoryList())

#根据产品id查询产品信息
@loginVerify
def getProductById(request):
    product_id = _post(request, "product_id")
    return HttpResponse(toJson(CurrentSystemService.getProductById(product_id)))

@loginVerify
def getCurrentSystemList(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(CurrentSystemService.getCurrentSystemList(search_text, page))
    return HttpResponse(json)

