from django.urls import path, include
from .views import nav, view_auth, search, item_detail, create_listing
from .views.create_complaint import CreateComplaint
from .views.create_listing import CreateListing
from .views.create_review import create_review
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'web'

urlpatterns=[
    path("", nav.home, name="home"),
    path("login/", view_auth.login, name="login"),
    path("logout/", view_auth.logout, name="logout"),
    path("register/", view_auth.register, name="register"),
    path('create_listing/', CreateListing.as_view(), name='create_listing'),
    path("home/", nav.home, name="home"),
    path('user/', nav.user, name= "user"),
    path("search/", search.search, name="search"),
    path("item/<int:pk>/", item_detail.detail, name="Item-detail"),
    path("item/<int:pk>/delete/", item_detail.delete, name="delete"),
    path("item/<int:pk>/edit/", item_detail.edit, name="edit"),
    path("category/<category>/", nav.cat_detail, name="category-detail"),
    # path("profile/", view_auth.profile, name="profile"),
    path("inbox/", include('conversation.urls')),
    path('complaint/create/<int:listing_id>/', CreateComplaint.as_view(), name='create_complaint'),
    path('reviews/create/<int:listing_id>/', create_review, name='create_review'),
] 

urlpatterns += staticfiles_urlpatterns()