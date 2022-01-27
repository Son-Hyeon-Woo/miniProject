from django.shortcuts import render, redirect
# View에 Model(Post 게시글) 가져오기
from .models import *
from config import settings
import os
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator

@login_required
def blog(request):
     # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    paginator = Paginator(postlist, 10)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'placeboard/blog.html',{'postlist':postlist , 'board_list':board_list})
    # , {'postlist':postlist}


def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'placeboard/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        postname = request.POST['postname']
        contents = request.POST['contents']
        mainphoto = request.FILES["mainphoto"]
        writer = request.user
        
        post = Post(
            postname=postname,
            contents=contents,
            mainphoto=mainphoto,
            writer=writer,
        )
        post.save()
        return redirect('/pb/blog')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'placeboard/new_post.html', context)

##게시글 삭제
def remove_post(request, pk):
 
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
      post.delete()
      return redirect('/pb/blog')
    return render(request, 'placeboard/remove_post.html', {'post': post})



def boardEdit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.postname = request.POST['postname']
        post.contents = request.POST['contents']
        post.mainphoto = request.FILES['mainphoto']
        post.writer = request.user
        
        post.save()
        return redirect('/pb/blog')

    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
            'post':post
        }
        return render(request, 'placeboard/update_post.html', context)

