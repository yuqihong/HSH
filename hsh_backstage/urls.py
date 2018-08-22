"""HSH_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# coding=utf-8

from django.conf.urls import url
from hsh_backstage.controller import MainController, CurrentSystemController

urlpatterns = [
    url(r'^main/$', MainController.main),
    url(r'^index/$', MainController.index),
    url(r'^bottom/$', MainController.bottom),
    url(r'^left/$', MainController.left),
    url(r'^top/$', MainController.top),
    
    url(r'^getCurrentSystemList/', CurrentSystemController.getCurrentSystemList),
    url(r'^addMenu/', CurrentSystemController.addMenu),
    url(r'^saveCurrentSystem/', CurrentSystemController.saveCurrentSystem),
    url(r'^delCurrentSystem/', CurrentSystemController.delCurrentSystem),
    url(r'^updateCurrentSystem/', CurrentSystemController.updateCurrentSystem),
    url(r'^getCategoryList/', CurrentSystemController.getCategoryList),
    url(r'^getCurrentSystem/', CurrentSystemController.getCurrentSystem),
    url(r'^getProductById/', CurrentSystemController.getProductById),
    url(r'^saveCurrentSystemImage/', CurrentSystemController.saveCurrentSystemImage),
    url(r'^updateCurrentSystemImage/', CurrentSystemController.updateCurrentSystemImage),
    url(r'^getEOLSystemList/', CurrentSystemController.getEOLSystemList),
    url(r'^getEOLSystem/', CurrentSystemController.getEOLSystem),
]
