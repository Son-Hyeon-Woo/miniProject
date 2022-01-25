from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

# Create your views here.
def mp(request):
    
    return render(request, 'mypage/mp.html')

def changePW(request):
    return render(request, 'mypage/changePW.html')
def changeEM(request):
    return render(request, 'mypage/changeEM.html')
def deleteID(request):
    return render(request, 'mypage/deleteID.html')