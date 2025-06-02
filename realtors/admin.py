from django.contrib import admin

# Register your models here.
from .models import Realtor  ## import the Listing class (captial letter)
class RealtorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email','phone','is_mvp' # Fields to display in the admin list view
    list_display_links = 'id', 'name'  # Fields that are clickable links
    list_editable = 'is_mvp', 'email','phone' # Fields that can be edited directly in the list view
    search_fields = 'name', # Fields to search in the admin interface
    list_per_page = 25  # Number of realtors to display per page in the admin interface
 
admin.site.register(Realtor, RealtorAdmin)
## place the Realtor model, and Realtor Admin menu in this admin.py to display




