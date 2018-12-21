from django.shortcuts import render
from django.http import HttpResponse
from .queries import TimesDefault, CWUDefault, SHJTDefault, TimesNormalSearch, CWUNormalSearch, SHJTNormalSearch, Country

# Create your views here.
def index(request):
    result = TimesDefault()
    countryMetrixDefault = Country('times', 2016, len(result))
    countryMetrixReformatDefault = []
    countryMetrixReformatDefault.append(CountryReformat(countryMetrixDefault, 2016))
    context = {'rankings': result, 'countryMetrix': countryMetrixReformatDefault}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = TimesNormalSearch(university, fromyear, toyear, limit)
        if (university != ""):
            searchResult = {'rankings': search}
        else:
            countryMetrixReformat = []
            if (toyear == "") :
                if (fromyear == ""):
                    fromyear = 2016
                if (limit == ""):
                    limitNum = 200
                else:
                    limitNum = limit
                countryMetrix = Country('times', fromyear, limitNum)
                countryMetrixReformat.append(CountryReformat(countryMetrix, fromyear))
                searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
            else:
                for year in range(int(fromyear), int(toyear)+1):
                    if (limit == ""):
                        limitNum = 200
                    else:
                        limitNum = limit
                    countryMetrix = Country('times', year, limitNum)
                    countryMetrixReformat.append(CountryReformat(countryMetrix, year))
                    searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
        return render(request, 'index.html', searchResult)
    return render(request, 'index.html', context)

def cwur(request):
    result = CWUDefault()
    countryMetrix = Country('cwur', 2015, len(result))
    countryMetrixReformat = []
    countryMetrixReformat.append(CountryReformat(countryMetrix, 2015))
    context = {'rankings': result, 'countryMetrix': countryMetrixReformat}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = CWUNormalSearch(university, fromyear, toyear, limit)
        if (university != ""):
            searchResult = {'rankings': search}
        else:
            countryMetrixReformat = []
            if (toyear == "") :
                if (fromyear == ""):
                    fromyear = 2016
                if (limit == ""):
                    limitNum = 200
                else:
                    limitNum = limit
                countryMetrix = Country('cwur', fromyear, limitNum)
                countryMetrixReformat.append(CountryReformat(countryMetrix, fromyear))
                searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
            else:
                for year in range(int(fromyear), int(toyear)+1):
                    if (limit == ""):
                        limitNum = 200
                    else:
                        limitNum = limit
                    countryMetrix = Country('cwur', year, limitNum)
                    countryMetrixReformat.append(CountryReformat(countryMetrix, year))
                    searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
        searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
        return render(request, 'index.html', searchResult)
    return render(request, 'cwur.html', context)

def shjt(request):
    result = SHJTDefault()
    countryMetrix = Country('shjt', 2015, len(result))
    countryMetrixReformat = []
    countryMetrixReformat.append(CountryReformat(countryMetrix, 2015))
    context = {'rankings': result, 'countryMetrix': countryMetrixReformat}
    if (request.GET):
        university = request.GET.dict().get("university")
        fromyear = request.GET.dict().get("from")
        toyear = request.GET.dict().get("to")
        limit = request.GET.dict().get("limitNum")
        search = SHJTNormalSearch(university, fromyear, toyear, limit)
        if (university != ""):
            searchResult = {'rankings': search}
        else:
            countryMetrixReformat = []
            if (toyear == "") :
                if (fromyear == ""):
                    fromyear = 2016
                if (limit == ""):
                    limitNum = 200
                else:
                    limitNum = limit
                countryMetrix = Country('shjt', fromyear, limitNum)
                countryMetrixReformat.append(CountryReformat(countryMetrix, fromyear))
                searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
            else:
                for year in range(int(fromyear), int(toyear)+1):
                    if (limit == ""):
                        limitNum = 200
                    else:
                        limitNum = limit
                    countryMetrix = Country('shjt', year, limitNum)
                    countryMetrixReformat.append(CountryReformat(countryMetrix, year))
                    searchResult = {'rankings': search, 'countryMetrix': countryMetrixReformat}
        return render(request, 'index.html', searchResult)
    return render(request, 'shanghai.html', context)

def CountryReformat(countryMetrix, year):
    country = []
    count = []
    percent = []
    for row in countryMetrix:
        country.append(row["Country"])
        count.append(row["UnivCount"])
        percent.append(row["percentage"])
    return {'year': year, 'country': country, 'count': count, 'percent': percent}
