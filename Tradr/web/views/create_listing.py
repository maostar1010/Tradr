from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from ..forms.form_listing import ListingForm ,EditlistingForm
from ..models import Listing, Image, Category
from django.contrib import messages 

class CreateListing(View):
    def get(self, request):
        form = ListingForm()
        categories = Category.objects.all()
        return render(request, 'web/create_listing.html', {'form': form, 'categories': categories})

    def post(self, request):
        form = ListingForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            for image in request.FILES.getlist('images'):
                Image.objects.create(listing=listing, image=image)
            form = ListingForm()
            messages.success(request, "Listing created successfully.")
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, 'web/create_listing.html', {'form': form})


