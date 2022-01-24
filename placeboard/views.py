from django.shortcuts import render,redirect
from .models import Post

def show(request):
    # 게시물 목록 출력
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'placeboard/list.html', context)

def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'placeboard/detail.html', context)


# blog.html 페이지를 부르는 blog 함수
def blog(request):
     # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'placeboard/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'placeboard/posting.html', {'post':post})

#게시글 작성 페이지
def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('blog')
    return render(request, 'placeboard/new_post.html')

##게시글 삭제
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'placeboard/remove_post.html', {'Post': post})
