from platform import java_ver
from django.shortcuts import render
from rank.models import Around_place
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from mapquiz.models import QuizLog


def finish(request):
    
    return render(request, 'rank/finish.html')

def near_food(request):
    around_place=Around_place.objects.all()
    
    
    

    return render(request, 'rank/near_food.html', { 'data': around_place })

def near_place(request):
    
    return render(request, 'rank/near_place.html')

def ranking(request):
    if request.method == 'POST':
        QuizLog.objects.create(
            user_id = request.POST['username'],
            point = request.POST['point'],
            play_time = request.POST['play_time']
        )
    return render(request, 'rank/ranking.html')