from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

"""
URL configuration for ERB6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings   ##go see settings.py to find MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static


## urlpatterns = []  ## a list of URL patterns, each pattern is a path to a view function
## functions within the [] are going to the public. 
urlpatterns = [
    ## Place the most frequent access page on the top, so that more effective
    path('', include('pages.urls', namespace='pages')), # Most popular page
    # Most ppl access empty '' 
    ## namespace give the name pages to distinguish the common name 'index'
    ## when you see empty string, go to pages.urls run pages
    path('listings/', include('listings.urls', namespace='listings')),  # listings app, second most popular
    ## realtors app has no Endpoint, so no need to include a URL
    path('admin/', admin.site.urls),  
    ## the admin console is pre-builded in Virtual Enviroment
    ] +  debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## Interal functions not going to public are putted behind '+' sign