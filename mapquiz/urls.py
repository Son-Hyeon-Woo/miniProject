from django.urls import path
from . import views

app_name = 'mapquiz'

urlpatterns = [
    path('quiz/', views.quiz),
    path('home/', views.index),
    path('quizend/', views.quizend),
    
]