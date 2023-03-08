from django.db import models
from django.contrib.auth.models import User
    
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    tag = models.CharField(max_length=200,null=True) # maybe we can get rid of it
    description = models.CharField(max_length=500, null=True)
    condition = models.CharField(max_length=200, null=True) # can we make it a drop down menu: new, like-new, mint, used


    def __str__(self):
        return self.title
    
class Image(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=False,blank=False)

    def __str__(self):
        return f"Image for {self.listing.title}: {self.image.name}"
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    # need to add html paths prob for dynamic nav bar when adding more categories later on

    def __str__(self):
        return self.title

class ListingCategory(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.title}: {self.listing.title}"
    
class Review(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_reviews')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_reviews')
    comment = models.CharField(max_length=500,null=True)
    rating = models.IntegerField()
    
    def __str__(self):
        return f"Review by {self.buyer.username} on {self.seller.username}"
    
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
    text = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"Complaint by {self.user.username} on {self.listing.title}"
    
class TransactionReport(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
    finalPrice = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f"Transaction Report of {self.listing.title}"