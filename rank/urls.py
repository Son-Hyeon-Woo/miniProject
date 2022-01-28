from django.urls import path
from . import views

urlpatterns = [

    path('near_food/', views.near_food),
    path('ranking/', views.ranking),

]