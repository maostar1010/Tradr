# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Numbers only please'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')