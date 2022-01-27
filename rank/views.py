from platform import java_ver
from django.shortcuts import render
from rank.models import Around_place
from mapquiz.models import Place
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from mapquiz.models import QuizLog
from django.contrib.auth.models import User
from django.db.models import Sum



from urllib.request import urlopen , Request
def finish(request):
    return render(request, 'rank/finish.html')

def near_food(request):
<<<<<<< HEAD
    place=Place.objects.filter(place_id=4)
    #place=Place.objects.all()
    around_place=Around_place.objects.filter(id_p=4)
    
    return render(request, 'rank/near_food.html',{ 'data': around_place ,'data2' : place})
=======
    around_place=Around_place.objects.all()
    return render(request, 'rank/near_food.html', { 'data': around_place })
>>>>>>> origin/master

def near_place(request):
    return render(request, 'rank/near_place.html')

def ranking(request):
<<<<<<< HEAD

    return render(request, 'rank/ranking.html')

    user_id = request.POST.get('username', False)
    point = request.POST.get('point', 0)
    play_time = request.POST.get('play_time', 0)
    
=======
>>>>>>> origin/master
    if request.method == 'POST':
        user_id = request.POST.get('username', False)
        point = request.POST.get('point', 0)
        play_time = request.POST.get('play_time', 0)

        QuizLog.objects.create(
            user_id = user_id,
            point = point,
            play_time = play_time
        )
<<<<<<< HEAD
    current_user = request.user
    print(User)

    data = {
        'point' : point,
        'username' : current_user.username,
        'play_time' : play_time
    }
    
    data = json.dumps(data)
    
    return render(request, 'rank/ranking.html', {'data': data})

=======
        d1 = {'user_id':user_id,'point':point,'play_time':play_time}
        temp =  json.dumps(d1)
        return JsonResponse(temp, safe=False)
    
    else:
        data = (QuizLog.objects
            .values('user_id')
            .annotate(pnt_sum=Sum('point'))
            .annotate(time_sum=Sum('play_time'))
            .values('user_id','pnt_sum','time_sum')
            .order_by('-pnt_sum'))
        data2 = []
        cnt = 1
        for i in data:
            print(i)
            print(i['user_id'])
            print(User.objects.get(id = i['user_id']))
            data2.append({'user_name' : User.objects.get(id = i['user_id']), 'pnt_sum' : i['pnt_sum'], 'time_sum':i['time_sum']})
            cnt += 1
            if cnt == 10:
                break;
            
        current_user = request.user
        current_user_point = data.get(user_id = current_user.id )
        

        
        return render(request, 'rank/ranking.html',{'data2':data2,'current_user':current_user,'current_user_point':current_user_point})
>>>>>>> origin/master
