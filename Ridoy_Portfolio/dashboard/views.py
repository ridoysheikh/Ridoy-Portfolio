from django.shortcuts import render
from Front_Pages.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("liged")
        else:
            pass

    return render(request, "dashboard/login.html",{})

def dashboard(request):
    return render(request, "dashboard/dashboard.html", {'title': "title",})

