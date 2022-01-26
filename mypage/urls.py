from django.urls import path
from . import views

urlpatterns = [
    path('mp/', views.mp),
    path('changePW/', views.changePW),
    path('changePW_e/', views.changePW_e),
    path('changeEM/', views.changeEM),
    path('deleteID/', views.deleteID),
]