from django.urls import path
from .views import auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("", auth.login, name="login"),
    path("register/", auth.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()