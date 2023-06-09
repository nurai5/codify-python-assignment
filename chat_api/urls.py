from django.urls import path
from .views import MessageCreateView, MessageListView

urlpatterns = [
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('messages/', MessageListView.as_view(), name='message-list'),
]
