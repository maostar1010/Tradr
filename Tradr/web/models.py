from django.db import models
from django.contrib.auth.models import User
    
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first())
    title = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    tag = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=False,blank=False)

    def __str__(self):
        return f"Image for {self.listing.title}: {self.image.name}"


