from multiprocessing.connection import answer_challenge
from platform import java_ver
from django.shortcuts import render
from .models import Place
import random, json
from django.contrib.auth.decorators import login_required

@login_required

def quiz(request):

    place_list = Place.objects.all()
    num = random.randrange(0,len(place_list))

    answer = place_list[num]
    latlong = {
        'name' : answer.place_name,
        'lat' : answer.place_lat,
        'long' : answer.place_long
    }
    latlong_json = json.dumps(latlong)
    return render( request, 'mapquiz/quiz.html', {'latlong_json': latlong_json,})

def index(request):

    return render(request, 'mapquiz/index.html')

def quizend(request):
    return render(request, 'mapquiz/quizend.html')