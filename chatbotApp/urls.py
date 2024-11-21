from django.contrib import admin
from django.urls import path,re_path
from .views import ChatBotView

urlpatterns = [
    path('chat', ChatBotView.as_view(), name='chatbot'),

]
