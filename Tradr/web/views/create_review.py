# in views.py
from django.shortcuts import render, redirect
from ..forms.form_review import ReviewForm
from ..models import Listing
from django.contrib import messages 


def create_review(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user, listing=listing)
        if form.is_valid():
            review = form.save()
            messages.success(request, "Review submitted. Thank you for your feedback.")
            return redirect('web:Item-detail', pk=listing_id)
    else:
        form = ReviewForm()
    return render(request, 'web/create_review.html', {'form': form})