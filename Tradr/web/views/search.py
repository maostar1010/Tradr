from django.shortcuts import render, redirect
from django.views import View
from ..forms.form_listing import ListingForm
from ..models import Listing, Image, Category

def search(request):
    query = request.GET.get('query','')
    listings = Listing.objects.all().filter(title__icontains = query)
    images = Image.objects.all()
        # curr_image = Image.objects.all()
    categories = Category.objects.all()
    

    print(images)
    print()


    return render(request,'web/search.html',{
            'listings' : listings,
            'images' : images,
            # 'curr_image' : curr_image,
            'categories' : categories,
            'query': query,
        })
    



    