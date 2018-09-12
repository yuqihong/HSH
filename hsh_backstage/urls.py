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
from hsh_backstage.controller import MainController, CurrentSystemController, AlertController,\
    SpareController, TipController, DocController

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
    
    url(r'^getAlert/', AlertController.getAlert),
    url(r'^saveAlert/', AlertController.saveAlert),
    url(r'^getTheirProductList/', AlertController.getTheirProductList),
    url(r'^getAlertList/', AlertController.getAlertList),
    url(r'^getUpdateAlert/', AlertController.getUpdateAlert),
    url(r'^updateAlert/', AlertController.updateAlert),
    url(r'^delAletrt/', AlertController.delAletrt),
    
    url(r'^getSpare/', SpareController.getSpare),
    url(r'^saveSpare/', SpareController.saveSpare),
    url(r'^getSpareList/', SpareController.getSpareList),
    url(r'^getSpareTypeList/', SpareController.getSpareTypeList),
    url(r'^getUpdateSpare/', SpareController.getUpdateSpare),
    url(r'^updateSpare/', SpareController.updateSpare),
    url(r'^delSpare/', SpareController.delSpare),
    
    url(r'^getTip/$', TipController.getTip),
    url(r'^getTipList/$',TipController.getTipList),
    url(r'^getUpdateTip/', TipController.getUpdateTip),
    url(r'^getTheirProductTip/', TipController.getTheirProductTip),
    url(r'^updateTip/', TipController.updateTip),
    url(r'^saveTip/', TipController.saveTip),
    url(r'^delTip/', TipController.delTip),
    
    url(r'^getDoc/', DocController.getDoc),
    url(r'^getDocList/', DocController.getDocList),
    url(r'^getProductList/', DocController.getProductList),
    url(r'^saveDoc/', DocController.saveDoc),
    url(r'^getUpdateDoc/', DocController.getUpdateDoc),
    url(r'^updateDoc/', DocController.updateDoc),
    url(r'^delDoc/', DocController.delDoc)
    
]
