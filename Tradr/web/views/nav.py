from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from web.models import Listing, Image, Category
# Create your views here.

def home(response):
    if response.user.is_authenticated:
        listings = Listing.objects.all()
        images = Image.objects.all()
        # curr_image = Image.objects.all()
        categories = Category.objects.all()

        return render(response, "web\home.html", {
            'listings' : listings,
            'images' : images,
            'categories' : categories,
        })
    return HttpResponseRedirect('/login')

def cat_detail(request, category):
    try:
        category_obj = get_object_or_404(Category, title__iexact=category)
        listings = Listing.objects.filter(category=category_obj).select_related('user')
        images = Image.objects.all()
    except Category.DoesNotExist:
        listings = []
        images = []

    categories = Category.objects.all()
    
    return render(request, "web/category.html", {
        'category': category_obj, 
        'categories': categories,
        'listings': listings,
        'images': images,
    })




