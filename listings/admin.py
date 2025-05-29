from django.contrib import admin
from .models import Listing  # Import the Listing class from models
from django.forms import NumberInput  # Import NumberInput for form field customization
from django.db import models  # Import models to use in formfield_overrides'
## define a class
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published','price', 'list_date','realtor'  # Fields to display in the admin list view
    list_display_links = 'id', 'title'  # Fields that are clickable links
    list_filter = 'realtor',  # Filters to apply in the admin interface
    list_editable = 'is_published', 'price'  # Fields that can be edited directly in the list view
    search_fields = 'title', 'description','address', 'price'  # Fields to search in the admin interface
    list_per_page = 25  # Number of listings to display per page in the admin interface
    ordering = ['-id']  # Default ordering of listings by list date in descending order
    prepopulated_fields = {'title': ('title',)}  # Automatically populate the slug field based on the title
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '10'})}}  # Use a number input for DecimalFields
    show_facets = admin.ShowFacets.ALWAYS
# Register the Listing model with the admin site using the ListingAdmin class

admin.site.register(Listing, ListingAdmin)  # Register the Listing model with the admin site
