from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import auth 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def mp(request):
    
    return render(request, 'mypage/mp.html')

def changePW_e(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST["origin_password"]
        if check_password(origin_password, user.password):
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('http://127.0.0.1:8000/map/home/')
            else:
                return render(request, 'mypage/changePW_e.html')
        else:
            return render(request, 'mypage/changePW_e.html')
    else:
        return render(request, 'mypage/changePW.html')

def changePW(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST["origin_password"]
        
        if check_password(origin_password, user.password):
            new_password = request.POST["new_password"]
            confirm_password = request.POST["confirm_password"]
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('http://127.0.0.1:8000/map/home/')
            else:
                return render(request, 'mypage/changePW_e.html')
        else:
            
            return render(request, 'mypage/changePW_e.html')
    else:
        return render(request, 'mypage/changePW.html')


def changeEM(request):
    if request.method == "POST":
        user = request.user
        origin_email = user.email
        new_email = request.POST["new_email"]

        if origin_email != new_email and new_email != '':
            user.email = new_email
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('http://127.0.0.1:8000/map/home/')
        else:
            return render(request, 'mypage/changeEM_e.html')
    else:
        return render(request, 'mypage/changeEM.html')


def changeEM_e(request):
    if request.method == "POST":
        user = request.user
        origin_email = user.email
        new_email = request.POST["new_email"]

        if origin_email != new_email:
            user.email = new_email
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('http://127.0.0.1:8000/map/home/')
        else:
            return render(request, 'mypage/changeEM_e.html')
    else:
        return render(request, 'mypage/changeEM.html')



def deleteID(request):
    if request.method == "POST":
        user = request.user
        
        # 아이디 가져오기
        text_confirm = '회원탈퇴'
        delete_confirm = request.POST["delete_confirm"]
        
        if text_confirm == delete_confirm:
            request.user.delete()
            return redirect('/')
        else:
            return render(request, 'mypage/deleteID_e.html')
    return render(request, 'mypage/deleteID.html')

def deleteID_e(request):
    if request.method == "POST":
        user = request.user
        
        # 아이디 가져오기
        text_confirm = '회원탈퇴'
        delete_confirm = request.POST["delete_confirm"]
        
        if text_confirm == delete_confirm:
            request.user.delete()
            return redirect('/')
        else:
            return render(request, 'mypage/deleteID_e.html')
    return render(request, 'mypage/deleteID.html')