from platform import java_ver
from django.shortcuts import render

def finish(request):
    
    return render(request, 'rank/finish.html')