# coding=utf-8
from django.shortcuts import render
from functools import wraps
from django.http.response import HttpResponse
from util.Util import toJson
import sys

def loginVerify(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            user = getSession(request, "user")
            agent = str(request.META.get('HTTP_USER_AGENT',None))
            if indexOf(agent,"MSIE")>=0 or indexOf(agent,"rv:")!=-1:
                return HttpResponse(toJson('请您勿使用IE浏览器访问!(推荐使用谷歌、火狐浏览器)'));
            if(user=='' or user==None):
                return render(request,'HSH_PROJECT/view/login.html')
        except:
            print(sys.exc_info())
            return render(request,'HSH_PROJECT/view/login.html')
        return func(request, *args, **kwargs)
    return wrapper

def getSession(request,key):
    session_value = None;
    try:
        session_value = request.session[key]
    except:
        print(sys.exc_info())
    return session_value
def indexOf(source,s):
    try:
        return source.index(s)
    except:
        return -1;
        