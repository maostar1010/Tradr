from django import forms
from ..models import Listing

class ListingForm(forms.ModelForm):
    
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Listing
        fields = ['title', 'price', 'condition', 'description', 'category',]
        widget = {
            'category' : forms.Select(),
            'condition' : forms.Select(),
            'description': forms.Textarea(attrs={"rows": 7, "cols": 40}),
        }



class EditlistingForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Listing
        fields = ['title', 'price', 'description', 'condition', 'category']
        widget = {
            'description': forms.Textarea(attrs={"rows": 7, "cols": 40}),
            'category' : forms.Select(),
            'condition' : forms.Select(),
        }
