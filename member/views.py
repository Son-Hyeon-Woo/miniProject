from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Member
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

#회원가입
def signup(request): 
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2']: 
            user = User.objects.create_user( 
                username=request.POST['username'], 
                password=request.POST['password1'], 
                email=request.POST['email'],
            ) 
            auth.login(request, user) 
            return redirect('/') 
        return render(request, 'signup.html') 
    return render(request, 'signup.html')
#로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 비밀번호를 확인해주세요.'})
    else:
        return render(request, 'login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')




# Create your views here.
