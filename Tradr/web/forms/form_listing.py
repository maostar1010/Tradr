from django import forms
from ..models import Listing

class ListingForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Listing
        fields = ['title', 'price', 'tag', 'description', 'condition', 'category']
        widget = {
            'category' : forms.Select()
        }