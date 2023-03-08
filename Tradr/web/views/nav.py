from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from web.models import Listing, Image, Category
# Create your views here.

def home(response):
    if response.user.is_authenticated:
        listings = Listing.objects.all()
        images = Image.objects.all()
        curr_image = Image.objects.get(id=1)
        categories = Category.objects.all()

        return render(response, "web\home.html", {
            'listings' : listings,
            'images' : images,
            'curr_image' : curr_image,
            'categories' : categories,
        })
    return HttpResponseRedirect('/login')

def books(response):
    return render(response, "web\\books.html", {})
