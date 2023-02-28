from django.urls import path
from .views import nav, view_auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("", nav.login, name="begin"),
    path("login/", view_auth.login, name="login"),
    path("register/", view_auth.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()