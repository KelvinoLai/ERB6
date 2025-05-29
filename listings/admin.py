from django.contrib import admin

from .models import Listing  # Import the Listing class from models

admin.site.register(Listing)  # Register the Listing model with the admin site
