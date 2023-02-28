from django.urls import path
from .views import nav, view_auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("", nav.login, name="begin"),
    path("login/", view_auth.login, name="login"),
    path("logout/", view_auth.logout, name="logout"),
    path("register/", view_auth.register, name="register"),
    path("home/", nav.home, name="home"),
]

urlpatterns += staticfiles_urlpatterns()