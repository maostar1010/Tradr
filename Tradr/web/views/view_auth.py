from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.forms.form_registration import UserRegForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout


# Create your views here.

def login(response):
    # if response.POST.get("login"):
    #   authentication

    return render(response, "web\login.html", {})

def register(response):

    # if already logged in, go to homepage
    if response.user.is_authenticated:
        # return redirect('/')

        # temporary logout
        logout(response)
        
    # storing the info entered
    if response.method =="POST":
        form = UserRegForm(response.POST)
        if form.is_valid(): # django default authentication
            user = form.save() # saving the info
            auth_login(response, user) # log in using the registered info
            return redirect('/') # redirect to home page

        else:
            for error in list(form.errors.values()):
                print(response, error)

    else:
        form = UserRegForm()

    return render(response, "web\\register.html", {'form': form})
