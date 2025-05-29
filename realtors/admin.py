from django.contrib import admin

# Register your models here.
from .models import Realtor  ## import the Listing class (captial letter)

admin.site.register(Realtor)




