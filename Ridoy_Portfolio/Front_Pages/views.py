from django.shortcuts import render

def home(request):
    title = "Home"
    return render(request, 'front/home.html',context={'title': title})

def resumes(request):
    title = "Resume"
    return render(request, 'front/resume.html',context={'title': title})

def contact(request):
    title = "Hire Me"
    return render(request, 'front/contact.html',context={'title': title})