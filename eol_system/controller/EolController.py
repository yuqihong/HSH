# coding=UTF-8
from django.shortcuts import render

def getEolSystemList(request):
    return render(request,'eol_system/view/index.html')

def getDataSheet(request):
    return render(request, 'eol_system/view/datasheet.html')

def getHomePage(request):
    return render(request, 'eol_system/view/homepage.html')