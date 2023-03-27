from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
# admin.site.register(Listing)
# admin.site.register(Image)
admin.site.register(Category)
admin.site.register(ListingCategory)
admin.site.register(Review)
admin.site.register(Complaint)
admin.site.register(TransactionReport)
admin.site.register(Condition)

class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Listing

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass