from django.urls import path
from . import views

app_name = 'help'

urlpatterns = [
    path('help/', views.help),
 
    path('why/', views.why),

    path('all/', views.all),
]