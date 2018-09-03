# coding=UTF-8
from util.Aop import loginVerify
from django.shortcuts import render
from util.Util import _post, toJson
import json
from django.http.response import HttpResponse
from hsh_backstage.service import AlertService
from util import Resp

@loginVerify
def getAlert(request):
    return render(request,'hsh_backstage/view/alert/alert.html')

@loginVerify
def addAlert(request):
    return render(request,'hsh_backstage/view/alert/add.html')

#添加Alert信息
@loginVerify
def saveAlert(request):
    dataJson = json.loads(_post(request, "data"))
    #先将信息添加到alert表中
    addAlertRow = AlertService.addAlert(dataJson)
    #在得到addAlertRow Id存到中间表中
    if (dataJson.get("their_product")!='' and dataJson.get("their_product")!=None):
        product_id = dataJson.get("their_product")
        AlertService.addAlertAndProduct(addAlertRow, product_id)
    if addAlertRow > 0:
        return HttpResponse(toJson({"state": "ok"}))
    else:
        return HttpResponse(toJson({"error": "添加失败"}))

#获取所有的Alert分页
@loginVerify
def getAlertList(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(AlertService.getAlertList(search_text, page))
    return HttpResponse(json)

#查询所有的产品名称
@loginVerify
def getTheirProductList(request):
    return HttpResponse(toJson(AlertService.getTheirProductList()))

#根据id获取alert信息
def getUpdateAlert(request):
    alert_id = _post(request, "alert_id")
    return HttpResponse(toJson(AlertService.getUpdateAlert(alert_id)))

#更新
def updateAlert(request):
    dataJson = json.loads(_post(request, "data"))
    #先根据alert_id更新中间表的产品Id
    AlertService.updateProductIdByAlertId(dataJson.get("alert_id"), dataJson.get("product_id"))
    #再修改alert属性
    updateAlertRow = AlertService.updateAlert(dataJson)
    respJson = {}
    if updateAlertRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));

#根据alert_id删除alert有关信息
def delAletrt(request):
    alert_id = _post(request, "alert_id")
    #先删除有关的中间表信息
    AlertService.delModdinByAlertId(alert_id)
    #再删除alert表信息
    delAlertRow = AlertService.delAlert(alert_id)
    respJson = {}
    if delAlertRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));