# coding=UTF-8
from django.shortcuts import render

def top(request):
    return render(request,'HSH_PROJECT/view/common/top.html')

def main(request):
    return render(request,'HSH_PROJECT/view/main.html')

def bottom(request):
    return render(request,'HSH_PROJECT/view/common/bottom.html')

def index(request):
    return render(request,'HSH_PROJECT/view/index.html')

def home(request):
    return render(request, 'HSH_PROJECT/view/home.html')

