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

    if password != password2:
            # 패스워드가 다르다는 에러 {'error':'에러문구'} 를 만들어서 전달
            return render(request, 'user/signup.html', {'error': '패스워드를 확인 해 주세요!'})
    else:
        if username == '' or password == '':
            # 사용자 저장을 위한 username과 password가 필수라는 것을 얘기 해 줍니다.
            return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다'})


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
