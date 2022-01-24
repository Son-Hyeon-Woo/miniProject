from django.shortcuts import render
from django.http import HttpResponse

def why(request):
    return HttpResponse('<h1>왜 안되노</h1>')

def help(request):
    return render(request,'help/helpme.html')


def all(request):
    return HttpResponse("""<!DOCTYPE html><html>
<head>
    <meta charset="utf-8">
    <title>게임 설명</title>
</head>
<body>
    <h1>게임 목적</h1>
    <h3>대구의 관광장소와 주변의 가볼만한 곳을 알려주기 위한 게임이다</h3>
    <h1>게임 방법</h1>
    <h2>1. 게임 시작하기<br>2. 로드뷰를 돌아다니며 현위치 장소 고르기</h2>
    <h3>*고른 위치와 정답 위치의 거리 차로 점수를 환산하니 신중히 고르십시오</h3>
</body>
</html>""")
    