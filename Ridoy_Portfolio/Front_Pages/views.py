from django.shortcuts import render
from .models import *


def home(request):
    title = "Home"
    navs_item = navs.objects.get(pk=1)
    return render(request, 'front/home.html',context={'title': title, 'navs': navs_item})

def resumes(request):
    title = "Resume"
    navs_item = navs.objects.get(pk=1)
    return render(request, 'front/resume.html',context={'title': title, 'navs': navs_item})

def contact(request):
    title = "Hire Me"
    navs_item = navs.objects.get(pk=1)
    return render(request, 'front/contact.html',context={'title': title, 'navs': navs_item})