from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listings = models.CharField(max_length=200)  # ForeignKey to Listings model can be added later
    listing_id = models.IntegerField()  # Assuming listing_id is an integer
## if the title of the listing are the same, need to retrieve the listing_id to distinguish them
## no need to build relationship of contacts with Listings 
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)  # EmailField for email addresses
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)  # Assuming user_id is an integer
    def __str__(self):      
        return self.name