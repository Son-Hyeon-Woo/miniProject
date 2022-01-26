from platform import java_ver
from django.shortcuts import render
from rank.models import Around_place
from mapquiz.views import quiz

from urllib.request import urlopen , Request
def finish(request):
    
    return render(request, 'rank/finish.html')

def near_food(request):
    around_place=Around_place.objects.all()

    
    # request = Request(url+)
    # getJson = json.loads(request.body)
    # print(json.dumps(need_id, sort_keys=True))
    return render(request, 'rank/near_food.html', { 'data': around_place })

def near_place(request):
    
    return render(request, 'rank/near_place.html')

def ranking(request):
    return render(request, 'rank/ranking.html')