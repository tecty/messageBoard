from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.
