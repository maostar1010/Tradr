from django.shortcuts import render, redirect
from django.views import View
from ..forms.form_listing import ListingForm
from ..models import Listing, Image

class CreateListing(View):
    def get(self, request):
        form = ListingForm()
        return render(request, 'create_listing.html', {'form': form})

    def post(self, request):
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            for image in request.FILES.getlist('images'):
                Image.objects.create(listing=listing, image=image)
            form = ListingForm()
            message = "Listing created successfully."
        else:
            message = "Please correct the errors below."
        return render(request, 'create_listing.html', {'form': form, 'message': message})