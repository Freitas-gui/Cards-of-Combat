from django.shortcuts import render, redirect
from authenticate.models import User
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        return redirect('url_allCards')
    else:
        return redirect('url_login')

def my_logout(request):
    logout(request)
    return redirect('url_login')