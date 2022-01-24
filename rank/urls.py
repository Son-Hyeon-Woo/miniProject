from django.urls import path
from . import views

urlpatterns = [
    path('finish/', views.finish),
    path('near_food/', views.near_food),
    path('near_place/', views.near_place),
]