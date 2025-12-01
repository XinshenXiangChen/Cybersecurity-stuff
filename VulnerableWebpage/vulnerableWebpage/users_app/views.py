from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def login(request):
    print(request)
    return render(request,'login.html')

    if request.method == 'POST':
        return my_view(request)
    return render(request,'login.html')


def my_view(request):
    if request.user_agent.is_mobile:
        return handle_mobile(request)
    return handle_desktop(request)

def handle_desktop(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.get(username=username)
    user_password = user.get_password(password)
    if user == None:
        return render(request,'login.html', {"error": "This user does not exist"})

    if password != user_password:
        return render(request,'login.html', {"error": "Passwords do not match"})

    else:
        return render(request,'login.html', {"message": "Login success"})

def handle_mobile(request):
    pass
