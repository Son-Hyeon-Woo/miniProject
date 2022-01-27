from multiprocessing.connection import answer_challenge
from platform import java_ver
from django.shortcuts import render, redirect
from .models import Place, QuizLog
import random, json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def quiz(request):
    place_list = Place.objects.all()
    num = random.randrange(0,len(place_list))
    current_user = request.user
    answer = place_list[num]
    
    latlong = {
        'ID': answer.place_id,
        'name' : answer.place_name,
        'lat' : answer.place_lat,
        'long' : answer.place_long
    }
    user = {
        'name' : current_user.id
    }
    
    latlong_json = json.dumps(latlong)
    user = json.dumps(user)
    
    request.session['place_id'] = answer.place_id
    
    return render( request, 'mapquiz/quiz.html', {'latlong_json': latlong_json, 'user' : user})

def index(request):
    return render(request, 'mapquiz/index.html')

def quizend(request):
    return render(request, 'mapquiz/quizend.html')