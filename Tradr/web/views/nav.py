from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(response):
    if response.user.is_authenticated:
        return render(response, "web\home.html", {})
    return HttpResponseRedirect('/login')
