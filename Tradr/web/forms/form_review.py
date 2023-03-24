# in forms.py
from django import forms
from ..models import Review

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, user=None, listing=None, **kwargs):
        self.user = user
        self.listing = listing
        super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['comment', 'rating']
        labels = {
            'comment': 'Comment',
            'rating': 'Rating'
        }

    def save(self, commit=True):
        review = super().save(commit=False)
        review.buyer = self.user
        review.seller = self.listing.user
        if commit:
            review.save()
        return review