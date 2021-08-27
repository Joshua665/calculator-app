from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Server Started')

def calculatorapp(request):
    return render(request, 'index.html')

def submitquery(request):
    q = request.GET['query']
    return HttpResponse(q)