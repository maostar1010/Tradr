from django.urls import path
from .views import auth, nav
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("", nav.login, name="begin"),
    path("login/", auth.login, name="login"),
    path("register/", auth.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()