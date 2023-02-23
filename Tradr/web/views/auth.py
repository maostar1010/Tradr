from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(response):
    # if response.POST.get("login"):
    #   authentication

    return render(response, "web\login.html", {})

def register(response):
    return render(response, "web\\register.html", {})
