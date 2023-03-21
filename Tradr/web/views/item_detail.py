from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from ..forms.form_listing import ListingForm
from ..models import Listing, Image, Category

def detail(request, pk):
    listings = get_object_or_404(Listing ,pk = pk)
    images =  Image.objects.filter(listing_id=pk)
    print(images)


    return render(request, "web/itemdescp.html", {
        'listings': listings,
        'I':images,
        
    })


def delete(request, pk):
    item = get_object_or_404(Listing, pk=pk, user = request.user)
    item.delete()
    return redirect('user')

def edit(request, pk):
    item = get_object_or_404(Listing, pk=pk, user = request.user)
    