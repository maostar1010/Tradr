from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:listing_pk>/', views.new_conversation, name='new'),
]

#Some of this code has been taken from https://www.youtube.com/watch?v=ZxMB6Njs3ck&t=7724s and modified for this website
