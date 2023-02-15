from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def api(request):
    if request.method == 'GET':
        if request.GET.get('name') == "bgimage" and request.GET.get('screen') == "Portrait":
            scr_size=request.GET.get('screen')
            images = bg_images.objects.filter(bg_mode=scr_size).values_list('bg_image', flat=True)
            images=list(images)
            return JsonResponse({'images':images})
        elif request.GET.get('name') == "bgimage" and request.GET.get('screen') == "Landscape":
            scr_size=request.GET.get('screen')
            images = bg_images.objects.filter(bg_mode=scr_size).values_list('bg_image', flat=True)
            images=list(images)
            return JsonResponse({'images':images})


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