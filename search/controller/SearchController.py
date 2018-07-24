'''
Created on 2018��6��28��

@author: yull
'''
from util.Util import _post, toJson
from search.service import SearchService
from django.http.response import HttpResponse

#����
def searchText(request):
    search_text = _post(request, "search_text")
    page = _post(request, "page")
    json = toJson(SearchService.search_text(search_text, page))
    return HttpResponse(json)
    