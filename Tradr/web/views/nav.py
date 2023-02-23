from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def login(response):
    return HttpResponseRedirect("/login")

def register(response):
    return render(response, "web\\register.html", {})
