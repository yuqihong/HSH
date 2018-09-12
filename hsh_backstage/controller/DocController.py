# coding=UTF-8
from util.Aop import loginVerify
from django.shortcuts import render
from util.Util import _post, toJson
import json
from django.http.response import HttpResponse
from hsh_backstage.service import DocService
from util import Resp

@loginVerify
def getDoc(request):
    return render(request,'hsh_backstage/view/doc/doc.html')

@loginVerify
def addAlert(request):
    return render(request,'hsh_backstage/view/alert/add.html')


#添加Doc信息
@loginVerify
def saveDoc(request):
    dataJson = json.loads(_post(request, "data")) 
    #先将信息添加到doc表中
    add_doc = DocService.addDoc(dataJson)
    #在得到add_doc Id存到中间表中
    if dataJson["their_product"] != '' and dataJson["their_product"] != None:
        product_id = dataJson["their_product"]
        DocService.addDocAndProduct(add_doc, product_id)
    if add_doc > 0:
        return HttpResponse(toJson({"state": "ok"}))
    else:
        return HttpResponse(toJson({"error": "添加失败"}))

#获取所有的Doc分页
@loginVerify
def getDocList(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(DocService.getDocList(search_text, page))
    return HttpResponse(json)

#查询所有的产品名称
@loginVerify
def getProductList(request):
    return HttpResponse(toJson(DocService.getProductList()))

#根据id获取doc信息
def getUpdateDoc(request):
    doc_id = _post(request, "doc_id")
    return HttpResponse(toJson(DocService.getUpdateDoc(doc_id)))

#更新
def updateDoc(request):
    dataJson = json.loads(_post(request, "data"))
    #先根据doc_id更新中间表的产品Id
    if dataJson["product_id"] != "":
        #判断中间表是否存在
        if DocService.getModdByDocId(dataJson["doc_id"]):
            DocService.updateProductIdByDocId(dataJson["product_id"], dataJson["doc_id"])
        else:
            #addDocAndProduct
            DocService.addDocAndProduct(dataJson["doc_id"], dataJson["product_id"])
    else:
        DocService.delModdinByDocId(dataJson["doc_id"])
    #再修改doc属性
    updateDocRow = DocService.updateDoc(dataJson)
    respJson = {}
    if updateDocRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson));

#根据doc_id删除doc有关信息
def delDoc(request):
    doc_id = _post(request, "doc_id")
    #先删除有关的中间表信息
    DocService.delModdinByDocId(doc_id)
    #再删除doc表信息
    delDocRow = DocService.delDoc(doc_id)
    respJson = {}
    if delDocRow > 0:
        respJson["result"] = Resp.SUCCESS
    else:
        respJson["result"] = Resp.ERROR
    return HttpResponse(toJson(respJson))