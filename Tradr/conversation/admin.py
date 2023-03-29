from django.contrib import admin

from .models import *

admin.site.register(Conversation)
admin.site.register(ConversationMessage)

# class MessageAdmin(admin.StackedInline):
#     model = ConversationMessage

# @admin.register(Conversation)
# class ConversationAdmin(admin.ModelAdmin):
#     inlines = [MessageAdmin]

#     class Meta:
#         model = Conversation

# @admin.register(ConversationMessage)
# class MessageAdmin(admin.ModelAdmin):
#     pass
