from web.models import User
from verify_email.email_handler import send_verification_email
from web.forms.form_registration import UserRegForm, UserAuthenticationForm, UserUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# import re

# Create your views here.

def register(response):
    # email_validate_pattern = r"^\S+|+@ucalgary.ca"
    if response.method == "POST":
        form = UserRegForm(response.POST)
        if form.is_valid():
            # if re.match(email_validate_pattern, email):
            inactive_user = send_verification_email(response, form)
            email       = form.cleaned_data.get('email')
            # form.save()
            # raw_pass    = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password = raw_pass)
            # auth_login(response, user)
            messages.success(response, "A verification email has been sent to {}. Please verify your email within the next 5 minutes using the link included in the email.".format(email))
            return redirect('/')
        else:
            messages.error(response, "Error: please use a valid ucalgary email and check the requirements for the password")
            # form = UserRegForm()
    else:
        form = UserRegForm()
    return render(response, "web/register.html", {'form': form})

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

def profile(response):
    if not response.user.is_authenticated:
        return redirect('/login')
    
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
