from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def login(request):
    if  request.method == 'POST':
        return my_view(request)
    else :
        return render(request,'login.html')

def is_admin_user_agent(request):

    user_agent = request.headers.get('User-Agent', '')  # Default to empty string if missing
    if 'Admin' in user_agent:
        print("True")
        return True

    else:
        return False


def my_view(request):
    if is_admin_user_agent(request):
        return handle_admin(request)
    return handle_desktop(request)

def handle_desktop(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == "admin":
        return render(request,'login.html', {"message": "You do not have the permissions to access this account"})
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request,'login.html', {"error": "This user does not exist"})

    user_password = user.get_password(password)
    if password != user_password:
        return render(request,'login.html', {"error": "Passwords do not match"})
    else:
        return render(request,'login.html', {"message": "Login success"})

def handle_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'admin_help_portal.html', {"error": "Username and password are required", "show_login": True})

        try:
            print(username)

            user = User.objects.get(username=username)

            user_password = user.get_password(password)
            
            if password != user_password:
                return render(request, 'admin_help_portal.html', {"error": "Invalid credentials", "show_login": True})
            else:
                # Successful login - show help portal with all users
                all_users = User.objects.all()
                return render(request, 'admin_help_portal.html', {
                    "message": "You captured the flag!",
                    "show_login": False,
                    "username": username,
                })
        except User.DoesNotExist:
            return render(request, 'admin_help_portal.html', {"error": "User does not exist", "show_login": True})
    else:
        # GET request - show login form
        return render(request, 'admin_help_portal.html', {"show_login": True})