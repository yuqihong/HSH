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
from HSH_PROJECT.controller import MainController, LoginController
from django.urls.conf import include

urlpatterns = [
    url(r'^current_system/', include("current_system.urls")),
    url(r'^eol_system/', include("eol_system.urls")),
    url(r'^feedback/', include("feedback.urls")),
    url(r'^quick_reference/', include("quick_reference.urls")),
    url(r'^search/', include("search.urls")),
    url(r'^view_show/', include("view_show.urls")),
    url(r'^home/', MainController.home),
    
    url(r'^accountLogin/', LoginController.accountLogin),
    url(r'^login/', LoginController.login),
    url(r'^loginOut/', LoginController.loginOut),
    url(r'^hsh_backstage/', include("hsh_backstage.urls")),
    
    
]
