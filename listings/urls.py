from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='listings'),  # listings index page
    path('<int:listing_id>', views.listing, name='listing'),  # listing detail page
    path('search', views.search, name='search'),  # search functionality
]