from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# manager for the custom model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# custom user class
class User(AbstractBaseUser):
    email               = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    title = models.CharField(max_length=200)
    # need to add html paths prob for dynamic nav bar when adding more categories later on

    def __str__(self):
        return self.title

class Condition(models.Model):
    condition = models.CharField(max_length=200)
    # need to add html paths prob for dynamic nav bar when adding more categories later on

    def __str__(self):
        return self.condition


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    # tag = models.CharField(max_length=200,null=True) # maybe we can get rid of it
    description = models.CharField(max_length=500, null=True)
    # icondition = models.CharField(max_length=200, null=True) # can we make it a drop down menu: new, like-new, mint, used
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, related_name='listing')
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE, null=True, related_name='listing')
    iamge = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE, null=True, related_name='images')
    image = models.ImageField(null=False,blank=False,upload_to='static')

    def __str__(self):
        return f"Image for {self.listing.title}: {self.image.name}"
    
    def delete(self, *args, **kwargs):
        print(self) # delete later
        self.image.delete()
        super().delete(*args, **kwargs)

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