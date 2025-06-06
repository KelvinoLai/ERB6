from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from contacts.forms import ContactForm

def contact(request):
    if request.method == "POST" :
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                # Logic to handle the case where the user has already contacted about this listing
                # For now, just redirect to a success page or render a message
                messages.error(request, "You have already contacted about this listing.")
                return redirect('listings:listing', listing_id=listing_id)
        contact = Contact(listings=listing, listing_id=listing_id, name=name, 
email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
            'kelvin398716@gmail.com',  # admin email address
            [realtor_email],  # Send to the realtor's email
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted, a realtor will get back to you soon.")
    return redirect("listings:listing", listing_id=listing_id)  # Redirect to the listing page after submission

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()  # Delete the contact with the given contact_id
    messages.success(request, "Contact deleted successfully.")
    return redirect("accounts:dashboard")  # Redirect to the dashboard or any other page after deletion    

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
       form = ContactForm(request.POST, instance=contact)
       if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully.")
            return redirect("accounts:dashboard")  # Redirect to the dashboard or any other page after update
    else:
        form = ContactForm(instance=contact)
    return render(request,"contacts/edit_message.html", {"form":form})  # Redirect to the dashboard or any other page after update
##    return render(request, 'contacts/edit_contact.html', {'contact': contact})  # Render the edit form with the contact data






"""
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST ['listing_id']
        listing = request.POST ['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                # Logic to handle the case where the user has already contacted about this listing
                # For now, just redirect to a success page or render a message
                messages.error(request, "You have already contacted about this listing.")
                return redirect('listings:listing', listing_id=listing_id)
        contact = Contact(listings=listing, listing_id=listing_id, name=name, 
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + '. Sign into the admin panel for more info.',
            'kelvin398716@gmail.com', # admin email address
            [realtor_email], # Send to the realtor's email
            fail_silently=False
        )           
        messages.success(request, "Your request has been submitted, a realtor will get back to you soon.")
        # If the user is authenticated, you can also save the user_id
        # Logic to handle the contact form submission
        # For now, just redirect to a success page or render a success message
        return redirect("listings:listing", listing_id=listing_id)  # Redirect to the dashboard or any other page after submission
  

def delete_contact(request, contact_id):
    # Logic to delete the contact with the given contact_id
    # For now, just render a success page or redirect
    return redirect("accounts:dashboard")  # Redirect to the dashboard or any other page after deletion
"""