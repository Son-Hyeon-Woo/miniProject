from django.contrib import admin
from django.urls import path
from .views import *
# index는 대문, blog는 게시판
from placeboard.views import blog, posting


app_name = 'placeboard'

urlpatterns = [
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    # path('blog/new_post/', new_post, name='new_post'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/remove/', remove_post, name='remove_post'),
]
