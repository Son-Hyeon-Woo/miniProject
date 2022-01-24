from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.show, name='show'),
    path('<int:postId>/', views.detail),
]