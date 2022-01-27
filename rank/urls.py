from django.urls import path
from . import views

urlpatterns = [

    path('near_food/', views.near_food),
    path('near_place/', views.near_place),
    path('ranking/', views.ranking),

]