from django.shortcuts import render
from django.http import HttpResponse
from .queries import TimesDefault, CWUDefault, SHJTDefault, TimesNormalSearch, CWUNormalSearch, SHJTNormalSearch

# Create your views here.
def index(request):
    result = TimesDefault()
    context = {'rankings': result}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = TimesNormalSearch(university, fromyear, toyear, limit)
        if (search == None):
            return render(request, 'index.html', {'text': 'Only Have Result For 2011-2016'})
        searchResult = {'rankings': search}
        return render(request, 'index.html', searchResult)
    return render(request, 'index.html', context)

def cwur(request):
    result = CWUDefault()
    context = {'rankings': result}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = CWUNormalSearch(university, fromyear, toyear, limit)
        if (search == None):
            return render(request, 'index.html', {'text': 'Only Have Result For 2012-2015'})
        searchResult = {'rankings': search}
        return render(request, 'index.html', searchResult)
    return render(request, 'cwur.html', context)

def shjt(request):
    result = SHJTDefault()
    context = {'rankings': result}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = SHJTNormalSearch(university, fromyear, toyear, limit)
        if (search == None):
            return render(request, 'index.html', {'text': 'Only Have Result For 2005-2015'})
        searchResult = {'rankings': search}
        return render(request, 'index.html', searchResult)
    return render(request, 'shanghai.html', context)
