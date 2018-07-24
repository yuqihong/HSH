# coding=UTF-8
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from django.http.response import HttpResponse
from HSH_PROJECT.service import UserService
from util import Base64
from util.Util import _post

def login(request):
    return render(request,'HSH_PROJECT/view/login.html')

def loginOut(request):
    request.session['user'] = None
    return render(request,'HSH_PROJECT/view/login.html')

@require_http_methods(['POST'])
def accountLogin(request):
    user_name = _post(request, "user_name")
    user_pass = _post(request, 'user_pass')
    # 返回给客户端的值
    params={}
    if(len(user_name) > 0 and len(user_pass) > 0):
        user = UserService.getUserLogin(user_name, Base64.md5hex(user_name+user_pass))
        if(len(user)>0):
            request.session['user'] =user[0]
            request.session.set_expiry(0)#关闭浏览器session失效
            params['result'] = "SUCCESS"
        else:
            params['result'] = "USER_ERROR"
    else:
        params['result'] = "USER_ERROR"
    return HttpResponse(json.dumps(params,ensure_ascii=False))