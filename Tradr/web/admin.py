from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Listing)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(ListingCategory)
admin.site.register(Review)
admin.site.register(Complaint)
admin.site.register(TransactionReport)