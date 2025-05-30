from django.shortcuts import render
from listings.models import Listing  # Import the Listing model to use in views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Import Paginator for pagination functionality

# Create your views here.
def index(request):
    listings = Listing.objects.all()   ## Select all listings from the database, everytime run once
                                     ## by the class in models.py
    paginator = Paginator(listings, 3)  ## Create a Paginator object with 3 listings per page, it's from Django Database
    page = request.GET.get('page')  ## Get the 'page' parameter from the request(from Frontend) it is the page number
    paged_listings = paginator.get_page(page)  ## Get the listings for the requested page, place the subset in 3 entites into the variable paged_listings
    context = {'listings' : paged_listings}  ## Add the paginated listings to the context    
   
    ##   another simple alternative here
    ##   return render(request, 'listings/listings.html', {'name' : "something" })
    return render(request, 'listings/listings.html', context)
def listing(request, listing_id):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')