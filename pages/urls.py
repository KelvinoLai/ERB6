from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('',views.index, name='index'),  
    path('about',views.about, name='about'),  
    #1st argument is url path, 2nd a function in views.py, 
    #3rd appear in Template later on and must be unique
]
