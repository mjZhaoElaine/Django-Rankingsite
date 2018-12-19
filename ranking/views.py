from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'name': 'mengjie', 'text': 'hello from index'}
    if (request.GET):
        university = request.GET.dict().get("university")
        successContext = {'name': university, 'text': 'have grabbed what I want'}
        return render(request, 'index.html', successContext)
    return render(request, 'index.html', context)

def cwur(request):
    context = {'name': 'mengjie', 'text': 'hello from cwur'}
    return render(request, 'cwur.html', context)

def shanghai(request):
    context = {'name': 'mengjie', 'text': 'hello from shanghai'}
    return render(request, 'shanghai.html', context)
