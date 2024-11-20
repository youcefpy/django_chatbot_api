from django.contrib import admin
from django.urls import path
from .views import ChatBotView

urlpatterns = [
    path('chat/', ChatBotView.as_view(), name='chatbot'),

]
