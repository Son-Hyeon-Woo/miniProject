from django.shortcuts import render
from django.http import HttpResponse
from .models import Around_place



def help(request):
    return render(request,'help/helpme.html')

def around(request):
    around_place=Around_place.objects.all()

    # result = ''
    # for c in around_place:
    #     result += c.id + '<br>'
    # return HttpResponse(result)
    #return HttpResponse ('<p>around_place</p>')
    return render(request,'help/around.html',{ 'data': around_place })

