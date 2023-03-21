from django.urls import path
from .views import nav, view_auth, search,item_detail
from .views.create_listing import CreateListing
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns=[
    path("", nav.home, name="home"),
    path("login/", view_auth.login, name="login"),
    path("logout/", view_auth.logout, name="logout"),
    path("register/", view_auth.register, name="register"),
    path('create_listing/', CreateListing.as_view(), name='create_listing'),
    path("home/", nav.home, name="home"),
    path("search/", search.search, name="search"),
    path("<int:pk>/", item_detail.detail, name="Item-detail"),
    path("<category>/", nav.cat_detail, name="category-detail"),
    path("profile/", view_auth.profile, name="profile"),
] 

urlpatterns += staticfiles_urlpatterns()