from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=200) ## charfield Cannot be unique 
    email = models.EmailField(max_length=50, unique=True, blank=True)  # Unique email for each realtor
    is_mvp = models.BooleanField(default=False)  # Most Valuable Person
    hire_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name
    
    