from django.urls import path
from . import views

urlpatterns = [
    path('finish/', views.finish),
]