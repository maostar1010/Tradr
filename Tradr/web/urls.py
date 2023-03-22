from django.urls import path
from .views import nav, view_auth
from .views.create_complaint import CreateComplaint
from .views.create_listing import CreateListing
from .views.create_review import create_review
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("", nav.home, name="home"),
    path("login/", view_auth.login, name="login"),
    path("logout/", view_auth.logout, name="logout"),
    path("register/", view_auth.register, name="register"),
    path('create_listing/', CreateListing.as_view(), name='create_listing'),
    path("home/", nav.home, name="home"),
    path("<category>/", nav.cat_detail, name="category-detail"),
    path('complaint/create/<int:listing_id>/', CreateComplaint.as_view(), name='create_complaint'),
    path('reviews/create/<int:listing_id>/', create_review, name='create_review'),
] 

urlpatterns += staticfiles_urlpatterns()