from django.shortcuts import render

def home(request):
    title = "Home"
    return render(request, 'front/home.html',context={'title': title})
