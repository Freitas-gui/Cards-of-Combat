from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request , 'home/home.html')

def my_logout(request):
    logout(request)
    return redirect('url_home')