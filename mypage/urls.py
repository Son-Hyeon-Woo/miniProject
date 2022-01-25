from django.urls import path
from . import views

urlpatterns = [
    path('mp/', views.mp),
    path('changePW/', views.changePW),
    path('changeEM/', views.changeEM),
    path('deleteID/', views.deleteID),
]