from django.contrib import admin
from django.urls import path
from .views import *
# index는 대문, blog는 게시판
from placeboard.views import *


app_name = 'placeboard'

urlpatterns = [
    # URL:pb/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:pb/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/remove/', remove_post, name='remove_post'),
    path('blog/<int:pk>/edit/', boardEdit, name='edit'),
    path('blog/<int:pk>/download/', download, name='download'),
    path('blog/<int:pk>/comment_create/', comment_create, name='comment_create'),


]


