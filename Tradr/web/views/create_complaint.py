from django.shortcuts import render, redirect
from django.views import View
from ..forms.form_listing import ListingForm
from ..forms.form_complaint import ComplaintForm
from ..models import Listing, Complaint
from django.contrib import messages 


class CreateComplaint(View):
    def get(self, request, listing_id):
        listing = Listing.objects.get(id=listing_id)
        form = ComplaintForm(initial={'listing': listing}, user=request.user, listing=listing)
        return render(request, 'complaint_form.html', {'form': form, 'listing': listing})

    def post(self, request, listing_id):
        listing = Listing.objects.get(id=listing_id)
        form = ComplaintForm(request.POST, initial={'listing': listing}, user=request.user, listing=listing)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.listing = listing
            complaint.save()
            messages.success(request, "Complaint received. Thank you for your feedback.")
            return redirect('/') # replace with your success URL
        return render(request, 'complaint_form.html', {'form': form, 'listing': listing})