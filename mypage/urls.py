from django.urls import path
from . import views

urlpatterns = [
    path('mp/', views.mp),
    path('changePW/', views.changePW),
    path('changePW_e/', views.changePW_e),
    path('changeEM/', views.changeEM),
    path('changeEM_e/', views.changeEM_e),
    path('deleteID/', views.deleteID),
    path('deleteID_e/', views.deleteID_e),
]