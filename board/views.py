from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, "login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('index')
    else:
        return render(request, 'login.html', {'error': '密码或帐号不正确'})


def signup(request):
    if request.method == 'GET':
        return render(request, "register.html")
    # POST
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']
    passwordAgain = request.POST['passwordAgain']
    if password != passwordAgain:
        return render(request, "register.html", {
            'error': '密码与确认密码不一致',
            'username': username,
            'name': name
        })
    user = User.objects.create_user(username, password=password)
    user.first_name = name[1:]
    user.last_name = name[0]
    user.save()
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('index')
    else:
        # Return an 'invalid login' error message.
        return render(request, "register.html", {
            'error': '用户名已经被注册',
            'username': username,
            'name': name
        })


def details(request, pk):
    msg = get_object_or_404(Message, pk=pk)


def create_msg(request):
    if request.method == 'GET':
        return redirect('index')
    title = request.POST['title']
    body = request.POST['body']
    user = request.user