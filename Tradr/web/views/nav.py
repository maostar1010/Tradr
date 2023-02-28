from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def login(response):
    return HttpResponseRedirect("/login")

def home(response):
    return render(response, "web\home.html", {})
