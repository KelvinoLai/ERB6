from django.shortcuts import render,get_object_or_404
from listings.models import Listing  # Import the Listing model to use in views
## from lisings app, models.py file, import the Listing class

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Import Paginator for pagination functionality
from listings.choices import price_choices, bedroom_choices, district_choices  # Import choices for filtering listings

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


    ## writeing SQL command here
    queryset_list = Listing.objects.order_by('-list_date')  ## Get all listings ordered by list date
    ##

### keywords from the search form in Search.html.
    if 'keywords' in request.GET:  ## Check if 'keywords' is in the GET request
        keywords = request.GET['keywords'] ## Get the value of 'keywords' from the GET request
        if keywords:  ## Trusive if keywords is not empty
            queryset_list = queryset_list.filter(description__icontains=keywords) ##double underscore ,icontains is a Django ORM filter that performs a case-insensitive search for the keywords in the description field of the Listing model.
                                                ## condition to filter listings by keywords
            ## Filter the queryset to include listings where the description contains the keywords, case-insensitive    
            ## icontains is case-insenitive.


    if 'title' in request.GET:  ## Check if 'keywords' is in the GET request
        title = request.GET['title'] ## Get the value of 'keywords' from the GET request
        if title:  ## Trusive if keywords is not empty
            queryset_list = queryset_list.filter(title__icontains=title) 

    if 'district' in request.GET:  ## Check if 'keywords' is in the GET request
        district = request.GET['district'] ## Get the value of 'keywords' from the GET request
        if district:  ## Trusive if keywords is not empty
            queryset_list = queryset_list.filter(district__iexact=district) #i means case-insensitive (exact match)

    if 'bedrooms' in request.GET:  ## Check if 'keywords' is in the GET request
        bedrooms = request.GET['bedrooms'] ## Get the value of 'keywords' from the GET request
        if bedrooms:  ## Trusive if keywords is not empty
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) 
            ##i means case-insensitive (lte menas less than or equal to match)

    if 'price' in request.GET:  ## Check if 'keywords' is in the GET request
        price = request.GET['price'] ## Get the value of 'keywords' from the GET request
        if price:  ## Trusive if keywords is not empty
            queryset_list = queryset_list.filter(price__lte=price) 
            ##i means case-insensitive (lte menas less than or equal to match)

##  FOR DEBUGGING PURPOSES
##  print(request.GET)  ## Print the GET request to the console for debugging purposes
##  FOR DEBUGGING PURPOSES


    context = {'price_choices': price_choices,
               'bedroom_choices' : bedroom_choices,
               'district_choices' : district_choices,
               'listings': queryset_list,
               'values': request.GET}  
    
               ## Add the listing to the context dictionary

    return render(request, 'listings/search.html', context)

"""  Three steps to and a function to the search page
1. import classes
2. define the function
3. return add the context render 
"""