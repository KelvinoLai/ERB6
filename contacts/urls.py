from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact/delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
    # path('success/', views.success, name='success'),  # Uncomment if you have a success view
    path('contact/edit/<int:contact_id>', views.edit_contact, name='edit_contact'),

    ## It's a virtual path, not a real path, views.edit_contact will handle the request, it's an actual link
]