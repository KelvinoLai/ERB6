from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
###  REMOVED after setted new pages    
##   return HttpResponse("<h1>Hello World</h1>")
#if no URL, reponse the message 'Hello world a as HTML
###
    pages_url = reverse('pages:index')
    return render(request, 'pages/index.html')

def about(request):
    pages_url = reverse('pages:about')
    return render(request, 'pages/about.html')
