from platform import java_ver
from django.shortcuts import render
from rank.models import Around_place

from mapquiz.views import quiz

import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from mapquiz.models import QuizLog
from django.contrib.auth.models import User


from urllib.request import urlopen , Request
def finish(request):
    
    return render(request, 'rank/finish.html')

def near_food(request):
    around_place=Around_place.objects.all()

    return render(request, 'rank/near_food.html', { 'data': around_place })

def near_place(request):
    
    return render(request, 'rank/near_place.html')

def ranking(request):

    return render(request, 'rank/ranking.html')

    user_id = request.POST.get('username', False)
    point = request.POST.get('point', 0)
    play_time = request.POST.get('play_time', 0)
    
    if request.method == 'POST':
        QuizLog.objects.create(
            user_id = user_id,
            point = point,
            play_time = play_time
        )
    current_user = request.user
    print(User)

    data = {
        'point' : point,
        'username' : current_user.username,
        'play_time' : play_time
    }
    
    data = json.dumps(data)
    
    return render(request, 'rank/ranking.html', {'data': data})

