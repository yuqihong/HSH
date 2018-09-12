# coding=UTF-8
from util.Aop import loginVerify
from django.shortcuts import render
from util.Util import _post, toJson
import json
from django.http.response import HttpResponse
from hsh_backstage.service import TipService
from util import Resp

@loginVerify
def getTip(request):
    return render(request,'hsh_backstage/view/tip/tip.html')

#添加tip信息
@loginVerify
def saveTip(request):
    dataJson = json.loads(_post(request, "data"))
    #先将信息添加到tip表中
    addTipRow = TipService.addTip(dataJson)
    #在得到addTiptRow Id存到中间表中
    if (dataJson.get("their_product")!='' and dataJson.get("their_product")!=None):
        product_id = dataJson.get("their_product")
        TipService.addTipAndProduct(addTipRow, product_id)
    if addTipRow > 0:
        return HttpResponse(toJson({"state": "ok"}))
    else:
        return HttpResponse(toJson({"error": "添加失败"}))

#获取所有的tip分页
@loginVerify
def getTipList(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(TipService.getTipList(search_text, page))
    return HttpResponse(json)

#查询所有的产品名称
@loginVerify
def getTheirProductTip(request):
    return HttpResponse(toJson(TipService.getTheirProductTip()))

#根据id获取tip信息
def getUpdateTip(request):
    tip_id = _post(request,"tip_id")
    return HttpResponse(toJson(TipService.getUpdateTip(tip_id)))

#更新
def updateTip(request):
    dataJson = json.loads(_post(request, "data"))
    #先根据tip_id更新中间表的产品Id
    if dataJson.get("product_id"):
        #判断中间表是否存在
        if TipService.getModdByTipId(dataJson.get("tip_id")):
            #update
            TipService.updateProductIdByTipId(dataJson.get("tip_id"), dataJson.get("product_id"))
        else:
            #addaddTipAndProduct
            TipService.addTipAndProduct(dataJson.get("tip_id"), dataJson.get("product_id"))
    else:
        TipService.delModdinByTipId(dataJson.get("tip_id"))
    #再修改tip属性
    updateTipRow = TipService.updateTip(dataJson)
    respJson = {}
    if updateTipRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));


#根据tip_id删除tip有关信息
def delTip(request):
    tip_id = _post(request, "tip_id")
    #先删除有关的中间表信息
    TipService.delModdinByTipId(tip_id)
    #再删除tip表信息
    delTipRow = TipService.delTip(tip_id)
    respJson = {}
    if delTipRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));