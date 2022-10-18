from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated # 로그인 된 사용자가 요청하는지 검사
        if user: # 로그인 되어있다면
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
        
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

def signin(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request,'user/signin.html')
    
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, username=username, password=password)

        if me:
            auth.login(request,me)
            return redirect('/')
        else:
            msg = {'error' : '유저이름 혹은 패스워드를 확인 해 주세요'}
            return render(request,'user/signin.html', msg)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request,'home.html')
    else:
        return redirect('/signin')
