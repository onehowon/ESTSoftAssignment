# blog/urls.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import path
from . import views  # 뷰 모듈을 임포트합니다.

urlpatterns = [
    path('login/', views.login_view, name='login'),  # '/login/' URL에 login_view를 연결합니다.
    # 다른 URL 패턴들을 필요에 따라 추가할 수 있습니다.
]


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인 되었습니다.')
            return redirect('login')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    return render(request, 'blog/login.html')