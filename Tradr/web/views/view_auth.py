from web.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from web.forms.form_registration import UserRegForm, UserAuthenticationForm, UserUpdateForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login(response):

    user = response.user
    if user.is_authenticated:
        return redirect('/')
    if response.method == 'POST':
        form    = UserAuthenticationForm(response.POST)
        email   = response.POST.get('email')
        password = response.POST.get('password')
        user    = authenticate(email=email, password=password)
        if user:
            auth_login(response, user)
            messages.success(response, "Logged In")
            return redirect("/")
        else:
            messages.error(response, "Invalid login: please try again")
    else:
        form = UserAuthenticationForm()
    return render(response, "web/login.html", {'form':form})
    
    #   authentication
    # context = {}
    # if response.user.is_authenticated:
    #     return redirect('/')
    
    # if response.method == "POST":
    #     form = UserAuthenticationForm(response.POST)
    #     email = response.POST.get('email')
    #     password = response.POST.get('password')
    #     user = authenticate(email=email, password=password)
    #     if user:
    #         auth_login(response.user)
    #         messages.success(response, "Logged in")
    #         return redirect("/")
    #     else:
    #         messages.error(response, "Please correct the following errors:")
    # else:
    #     form = UserAuthenticationForm()
    # context['form']=form
    # return render(response, "web\\login.html", context)
    #     if form.is_valid():
    #         user = authenticate(
    #             username=form.cleaned_data["username"],
    #             password=form.cleaned_data["password"],
    #         )
    #         if user is not None:
    #             auth_login(response, user)
    #             messages.success(response, f"Welcome back, <b>{user.username}</b>!")
    #             return redirect("/")
    #     else:
    #         for error in list(form.error.values()):
    #             messages.error(response, error)

    # form = AuthenticationForm()
    # return render(response, "web\login.html", {"form":form})

@login_required
def logout(response):
    auth_logout(response)
    messages.success(response, "Logged out successfully")
    # return render(response, "web\\logout.html", {})
    return redirect("/")
    
    # return render(response, "web\logout.html", {})

def register(response):
    if response.method == "POST":
        form = UserRegForm(response.POST)
        if form.is_valid():
            form.save()
            email       = form.cleaned_data.get('email')
            raw_pass    = form.cleaned_data.get('password1')
            user = authenticate(email=email, password = raw_pass)
            auth_login(response, user)
            messages.success(response, "You have been registered as {}".format(response.user.username))
            return redirect('/')
        else:
            messages.error(response, "Error: please correct the errors")
            form = UserRegForm()
    else:
        form = UserRegForm()

    
    # if already logged in, go to homepage
    # if response.user.is_authenticated:
    #     # return redirect('/')

    #     # temporary logout
    #     auth_logout(response)
        
    # # storing the info entered
    # if response.method =="POST":
    #     form = UserRegForm(response.POST)
    #     if form.is_valid(): # django default authentication
    #         user = form.save() # saving the info
    #         auth_login(response, user) # log in using the registered info
    #         messages.success(response, f"New account created: {user.username}")
    #         return redirect('/') # redirect to home page

    #     else:
    #         for error in list(form.errors.values()):
    #             messages.error(response, error)

    # else:
    #     form = UserRegForm()

    return render(response, "web/register.html", {'form': form})

def profile(response):
    if not response.user.is_authenticated:
        return redirect('login')
    
    if response.method == 'POST':
        form = UserUpdateForm(response.POST, instance = response.user)
        if form.is_valid():
            form.save()
            messages.success(response, "Profile updated successfully")
        else:
            messages.error(response, "Error: please correct the errors")
    
    else:
        form = UserUpdateForm(
            initial={
            'email':response.user.email,
            'username':response.user.username,
            }
        )
    
    return render(response, "web/userprofile.html", {'form':form})