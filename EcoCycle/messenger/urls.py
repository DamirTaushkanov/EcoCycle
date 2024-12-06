from django.urls import path
from messenger.views import chat_list, chat_detail

urlpatterns = [
    path('chat_list/', chat_list),
    path('chat_detail/', chat_detail)
]
