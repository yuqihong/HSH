# coding=UTF-8
from django.shortcuts import render
from django.http.response import HttpResponse
from current_system.service import CurrentService
from util.Util import toJson, _post

def getCurrentSystemList(request):
    return render(request,'current_system/view/index.html')

def getCurrentSystem(request):
    return render(request, 'current_system/view/current_system.html')

def getDataSheet(request):
    return render(request, 'current_system/view/datasheet.html')

def getHomePage(request):
    return render(request, 'current_system/view/homepage.html')

#获取分类集合
def getCurrentSystemCategory(request):
    return HttpResponse(CurrentService.getCurrentSystemCategory())

#获取产品集合
def getCurrentSystemProduct(request):
    json = toJson(CurrentService.getCurrentSystemProduct())
    return HttpResponse(json)

#获取产品集合1
def getCurrentSystemProduct_EOL_0(request):
    json = toJson(CurrentService.getCurrentSystemProduct_EOL_0())
    return HttpResponse(json)

#获取产品集合2
def getCurrentSystemProduct_EOL_1(request):
    json = toJson(CurrentService.getCurrentSystemProduct_EOL_1())
    return HttpResponse(json)

#通过productName查询信息
def selectCurrentSystemByProductName(request):
    product_name = _post(request, "product_name")
    json = toJson(CurrentService.selectCurrentSystemByProductName(product_name))
    return HttpResponse(json)
