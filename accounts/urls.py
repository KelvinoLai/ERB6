from django.urls import path
from . import views

app_name = 'accounts'  # This is the namespace for the accounts app
urlpatterns = [
    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login, name='login'),  # Login page
    path('logout/', views.logout, name='logout'),  # Logout page
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard

]
