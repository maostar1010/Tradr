from django import forms
from ..models import Complaint

class ComplaintForm(forms.ModelForm):
    def __init__(self, *args, user=None, listing=None, **kwargs):
        self.user = user
        self.listing = listing
        super().__init__(*args, **kwargs)

    class Meta:
        model = Complaint
        fields = ['text']