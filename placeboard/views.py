from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
# View에 Model(Post 게시글) 가져오기
from .models import *
from config import settings
import os
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
import urllib.parse
import json
from django.contrib import messages
from django.db.models import Count
from django.forms.models import model_to_dict

@login_required
def blog(request):
    
    data = (Comment.objects
    .values('post_id')
    .annotate(cnt_sum=Count('id'))
    .values('post_id','cnt_sum')
    .order_by('-post_id'))
    data2 = Post.objects.all()
    postlist = Post.objects.order_by('-id')

    
    cnt_comment = {}
    cnt = 1
    for i in postlist:
        key = i.id
        postlist
        try:
            cnt_comment[cnt] = data.get(post_id = i.id)['cnt_sum']
        except:
            cnt_comment[cnt] = 0
        cnt += 1

    
    paginator = Paginator(postlist, 10)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'placeboard/blog.html',{'postlist':postlist , 'board_list':board_list,'cnt_comment':cnt_comment})
    # , {'postlist':postlist}


def posting(request, pk):
    if request.method == 'POST':
        pkk = request.POST.get('id')
        comment = Comment.objects.get(pk=pkk)
        user_id = request.user.id
        if user_id == comment.writer_id:    
            comment.delete()
            data = {'pk': pk}
            data =  json.dumps(data)
            return JsonResponse(data, safe=False)
        else:
            data = {'pk': -1}
            data =  json.dumps(data)
            return JsonResponse(data, safe=False)

    else:
        # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
        post = Post.objects.get(pk=pk)

        comments = post.comment_set.order_by('-id').all()
    
        context = {'post': post, 'comments': comments}
        # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
        return render(request, 'placeboard/posting.html', context)


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
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        if post.writer == request.user:
            post.delete()
            return redirect('/pb/blog')
        else:
            return render(request, 'placeboard/remove_post_error.html', {'post': post})
    return render(request, 'placeboard/remove_post.html', {'post': post})



def boardEdit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        if post.writer == request.user:
            post.delete()
            post.postname = request.POST['postname']
            post.contents = request.POST['contents']
            post.mainphoto = request.FILES['mainphoto']
            post.writer = request.user
            
            post.save()
            return redirect('/pb/blog')
        else:
            return render(request, 'placeboard/remove_post_error.html', {'post': post})
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
            'post':post
        }
        return render(request, 'placeboard/update_post.html', context)


def download(request, pk):
    uploadFile = Post.objects.get(id=pk)
    filepath = str(settings.BASE_DIR) + ('/media/%s' % uploadFile.mainphoto)
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as ab:
        response = HttpResponse(ab, content_type='application/octet-stream')
        #response['Content-Disposition'] = 'attachment; filename=*=UTF-8'' 디아크_BhFhDxT.jpg'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(urllib.parse.quote(filename.encode('utf-8')))
        return response



def comment_create(request,pk):
    if request.method == 'POST':
        content = request.POST.get('content')
        writer = request.user
        post=get_object_or_404(Post,pk=pk)
        
        if not content:
            messages.info(request,'입력해주세요.')
            return redirect('placeboard:posting',pk)
        
        Comment.objects.create(post=post, writer=writer, comment=content)

        return redirect('placeboard:posting', pk)   
    
    

