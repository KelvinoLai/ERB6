from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
###  REMOVED after setted new pages    
##   return HttpResponse("<h1>Hello World</h1>")
#if no URL, reponse the message 'Hello world a as HTML
###
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
