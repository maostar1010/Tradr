from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from web.models import Listing, Category

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, listing_pk):
    categories = Category.objects.all()
    listing = get_object_or_404(Listing, pk=listing_pk)

    if listing.user == request.user:
        return redirect('conversation:inbox')
    
    conversations = Conversation.objects.filter(listing=listing).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)
    
    else:
        form = ConversationMessageForm()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(listing=listing)
            conversation.members.add(request.user)
            conversation.members.add(listing.user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('web:Item-detail', pk=listing_pk)
    
    return render(request, 'conversation/new.html', {
        'form': form,
        'categories': categories,
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    categories = Category.objects.all()
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'categories': categories,
    })

@login_required
def detail(request, pk):
    categories = Category.objects.all()
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'categories': categories,
    })
