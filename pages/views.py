from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing  # Import the Listing model to use in views
from realtors.models import Realtor  # Import the Realtor model to use in views
# Create your views here.
def index(request):

###  REMOVED after setted new pages    
##   return HttpResponse("<h1>Hello World</h1>")
#if no URL, reponse the message 'Hello world a as HTML
###
## older version    pages_url = reverse('pages:index')

                                                            ## is_published=True 
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]  # Select all listings from the database, ordered by list date, only published listings in 3 itmes                                                            
    context = {"listings": listings}  # Add the listings to the context
    return render(request, 'pages/index.html', context)  # Render the index template with the listings context
## objecits is a manager to communicate with the database, and we use it to filter and order the listings.
## build the sql command but not excuted until [:3] add this list.  


"""
def about(request):
    pages_url = reverse('pages:about')
    return render(request, 'pages/about.html')
"""
def about(request):
    ## method 1: Get all realtors and order by hire date, filter MVP realtors
    realtors_base = Realtor.objects.all()  # Get all realtors from the database
    realtors = realtors_base.order_by('-hire_date')  # Order realtors by hire date
    mvp_realtors = realtors_base.filter(is_mvp=True)  # Filter to get only MVP realtors

    """
    ## method 2: Get all realtors and order by hire date, filter MVP realtors 
    realtors = Realtor.objects.order_by('-hire_date')  # Get all realtors ordered by hire date
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)  # Get only MVP realtors
    ## method 2:
    """
 
    context = { 'realtors': realtors,'mvp_realtors': mvp_realtors}  # Add the realtors and MVP realtors to the context
    # Render the about template with the realtors context
    return render(request, 'pages/about.html', context)  
# Render the about template with the realtors context