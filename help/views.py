from django.shortcuts import render
from django.http import HttpResponse


def help(request):
    return render(request,'help/helpme.html')
