from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from quiz.views import get_question 

urlpatterns = [
    path('questions/', get_question, name='get_question'),
    path('', lambda request: render(request, 'quiz.html'), name='quiz')
]
