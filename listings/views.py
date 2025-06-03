from django.shortcuts import render,get_object_or_404
from listings.models import Listing  # Import the Listing model to use in views
## from lisings app, models.py file, import the Listing class

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Import Paginator for pagination functionality

# Create your views here.
def index(request):
    listings = Listing.objects.all()   ## Select all listings from the database, everytime run once
                                     ## by the class in models.py
    paginator = Paginator(listings, 3)  ## Create a Paginator object with 3 listings per page, it's from Django Database
    page = request.GET.get('page')  ## Get the 'page' parameter from the request(from Frontend) it is the page number
    paged_listings = paginator.get_page(page)  ## Get the listings for the requested page, place the subset in 3 entites into the variable paged_listings
    context = {'listings' : paged_listings} ## Add the paginated listings to the context 
 
   
    ##   another simple alternative here
    ##   return render(request, 'listings/listings.html', {'name' : "something" })
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):  ##get one record only
    listing = get_object_or_404(Listing, pk=listing_id)  ## Get the listing with the given ID from the database
    ## Listing class here, we treat it as a table in the database

    context = {'listing': listing}  ## Add the listing to the context dictionary
    return render(request, 'listings/listing.html', context)  ## Render the listing template with the context
def search(request):
    return render(request, 'listings/search.html')