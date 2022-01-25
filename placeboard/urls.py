from django.contrib import admin
from django.urls import path
from .views import *
# index는 대문, blog는 게시판
from placeboard.views import blog, posting
# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/remove/', remove_post, name='remove_post'),
]+ static(
settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

# 이미지 URL 설정
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

