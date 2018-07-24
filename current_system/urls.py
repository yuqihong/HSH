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
from django.conf.urls import url
from current_system.controller import CurrentController

urlpatterns = [
    url(r'^getCurrentSystemList/', CurrentController.getCurrentSystemList),
    url(r'^getCurrentSystem/', CurrentController.getCurrentSystem),
    url(r'^getDataSheet/', CurrentController.getDataSheet),
    url(r'^getCurrentSystemCategory/', CurrentController.getCurrentSystemCategory),
    url(r'^getCurrentSystemProduct_EOL_0/', CurrentController.getCurrentSystemProduct_EOL_0),
    url(r'^getCurrentSystemProduct_EOL_1/', CurrentController.getCurrentSystemProduct_EOL_1),
    url(r'^getCurrentSystemProduct/', CurrentController.getCurrentSystemProduct),
    url(r'^selectCurrentSystemByProductName/', CurrentController.selectCurrentSystemByProductName),
    url(r'^getHomePage/', CurrentController.getHomePage),
    
]
