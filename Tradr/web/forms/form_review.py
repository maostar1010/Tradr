from django import forms
from ..models import Review

class ComplaintForm(forms.ModelForm):
    def __init__(self, *args, user=None, listing=None, **kwargs):
        self.user = user
        self.listing = listing
        super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['comment', 'rating']