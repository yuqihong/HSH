# coding=UTF-8
from django.shortcuts import render
from util.Aop import loginVerify

@loginVerify
def main(request):
    return render(request,'hsh_backstage/view/main.html')

@loginVerify
def index(request):
    return render(request,'hsh_backstage/view/index.html')

@loginVerify
def left(request):
    return render(request,'hsh_backstage/view/common/left.html')

@loginVerify
def top(request):
    return render(request,'hsh_backstage/view/common/top.html')

@loginVerify
def bottom(request):
    return render(request,'hsh_backstage/view/common/bottom.html')

