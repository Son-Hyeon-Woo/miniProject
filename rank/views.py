from platform import java_ver
from django.shortcuts import render

def finish(request):
    
    return render(request, 'rank/finish.html')

def near_food(request):
    
    return render(request, 'rank/near_food.html')

def near_place(request):
    
    return render(request, 'rank/near_place.html')

def ranking(request):
    return render(request, 'rank/ranking.html')