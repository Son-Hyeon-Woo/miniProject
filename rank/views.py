from platform import java_ver
from django.shortcuts import render
from rank.models import Around_place
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from mapquiz.models import QuizLog
from django.contrib.auth.models import User
from django.db.models import Sum
from mapquiz.models import Place
from django.contrib.auth.decorators import login_required


@login_required
def near_food(request):
    a=request.session.get('place_id', '0')
    print(a)
    place=Place.objects.filter(place_id=a)
    around_place=Around_place.objects.filter(id_p=a)
    
    return render(request, 'rank/near_food.html',{ 'data': around_place ,'data2' : place})

@login_required
def ranking(request):
    if request.method == 'POST':
        user_id = request.POST.get('username', False)
        point = request.POST.get('point', 0)
        play_time = request.POST.get('play_time', 0)

        QuizLog.objects.create(
            user_id = user_id,
            point = point,
            play_time = play_time
        )
        data = {'good':'잘 저장되었음!'}
        data =  json.dumps(data)
        return JsonResponse(data, safe=False)
    
    else:
        data = (QuizLog.objects
            .values('user_id')
            .annotate(pnt_sum=Sum('point'))
            .annotate(time_sum=Sum('play_time'))
            .values('user_id','pnt_sum','time_sum')
            .order_by('-pnt_sum'))
        data2 = []
        cnt = 0
        for i in data:
            data2.append({'user_name' : User.objects.get(id = i['user_id']), 'pnt_sum' : i['pnt_sum'], 'time_sum':i['time_sum']})
            cnt += 1
            if cnt == 10:
                break
        current_user = request.user
        current_user_point = data.get(user_id = current_user.id )
        return render(request, 'rank/ranking.html',{'data2':data2,'current_user':current_user,'current_user_point':current_user_point})
