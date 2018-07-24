'''
Created on 2018年6月28日

@author: yull
'''
from util.Util import _post, toJson
from search.service import SearchService
from django.http.response import HttpResponse

#查找
def searchText(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(SearchService.search_text(search_text, page))
    return HttpResponse(json)
    