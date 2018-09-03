# coding=UTF-8
from util.Aop import loginVerify
from django.shortcuts import render
from util.Util import _post, toJson
import json
from django.http.response import HttpResponse
from util import Resp
from hsh_backstage.service import SpareService, AlertService

@loginVerify
def getSpare(request):
    return render(request,'hsh_backstage/view/spare/spare.html')

#添加Alert信息
@loginVerify
def saveSpare(request):
    dataJson = json.loads(_post(request, "data"))
    #先将信息添加到Spare表中
    addSpareRow = SpareService.addSpare(dataJson)
    #在得到addAlertRow Id存到中间表中
    if (dataJson.get("their_product")!='' and dataJson.get("their_product")!=None):
        product_id = dataJson.get("their_product")
        SpareService.addSpareAndProduct(addSpareRow, product_id)
    if addSpareRow > 0:
        return HttpResponse(toJson({"state": "ok"}))
    else:
        return HttpResponse(toJson({"error": "添加失败"}))

#获取所有的Alert分页
@loginVerify
def getSpareList(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(SpareService.getSpareList(search_text, page))
    return HttpResponse(json)

#查询所有的spare type信息
@loginVerify
def getSpareTypeList(request):
    return HttpResponse(toJson(SpareService.getSpareTypeList()))

#根据id获取spare信息
def getUpdateSpare(request):
    spare_id = _post(request, "id")
    return HttpResponse(toJson(SpareService.getUpdateSpare(spare_id)))

#更新
def updateSpare(request):
    dataJson = json.loads(_post(request, "data"))
    #先根据spare_id更新中间表的产品Id
    if dataJson.get("their_product"):
        #判断中间表中是否存在
        if SpareService.getModdBySpareId(dataJson.get("spare_id")):
            #update
            SpareService.updateProductIdBySpareId(dataJson.get("spare_id"), dataJson.get("their_product"))
        else:
            #add
            SpareService.addSpareAndProduct(dataJson.get("spare_id"), dataJson.get("their_product"))
    else:
        SpareService.delModdinBySpareId(dataJson.get("spare_id"))
    #再修改spare属性
    updateSpareRow = SpareService.updateSpare(dataJson)
    respJson = {}
    if updateSpareRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));

#根据alert_id删除alert有关信息
def delSpare(request):
    spare_id = _post(request, "spare_id")
    #先删除有关的中间表信息
    SpareService.delModdinBySpareId(spare_id)
    #再删除alert表信息
    delSpareRow = SpareService.delSpare(spare_id)
    respJson = {}
    if delSpareRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));