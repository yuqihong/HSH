# coding=UTF-8
from django.http.response import HttpResponse
from django.shortcuts import render

def getViewShow(request):
    return render(request,'view_show/view/view_show.html')