from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from web.models import Listing, Image, Category
# Create your views here.

def home(response):
    if response.user.is_authenticated:
        listings = Listing.objects.all()
        images = Image.objects.all()
        # curr_image = Image.objects.all()
        categories = Category.objects.all()

        return render(response, "web/home.html", {
            'listings' : listings,
            'images' : images,
            'categories' : categories,
        })
    return HttpResponseRedirect('/login')

def inbox(response):
        if response.user.is_authenticated:
            return render(response, "web/inbox.html", {
                'inbox' : inbox,
            })

def cat_detail(response, category):
    categories = Category.objects.all()
    # can we filter listings for the specific category chosen here?
    #  listings = listing....??
    # then pass the listings and print all of them in the category.html
    return render(response, "web/category.html", {'category':category, 'categories': categories})
