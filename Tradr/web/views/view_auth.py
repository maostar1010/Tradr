from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.forms.form_registration import UserRegForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login(response):
    # if response.POST.get("login"):
    #   authentication
    if response.user.is_authenticated:
        return redirect('/home')
    
    if response.method == "POST":
        form = AuthenticationForm(response, data=response.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth_login(response, user)
                messages.success(response, f"Welcome back, <b>{user.username}</b>!")
                return redirect("/home")
        else:
            for error in list(form.error.values()):
                messages.error(response, error)

    form = AuthenticationForm()
    return render(response, "web\login.html", {"form":form})

@login_required
def logout(response):
    auth_logout(response)
    messages.info(response, "Logged out successfully")
    return redirect("login")
    
    # return render(response, "web\logout.html", {})

def register(response):

    # if already logged in, go to homepage
    if response.user.is_authenticated:
        # return redirect('/')

        # temporary logout
        auth_logout(response)
        
    # storing the info entered
    if response.method =="POST":
        form = UserRegForm(response.POST)
        if form.is_valid(): # django default authentication
            user = form.save() # saving the info
            auth_login(response, user) # log in using the registered info
            messages.success(response, f"New account created: {user.username}")
            return redirect('/home') # redirect to home page

        else:
            for error in list(form.errors.values()):
                messages.error(response, error)

    else:
        form = UserRegForm()

    return render(response, "web\\register.html", {'form': form})
